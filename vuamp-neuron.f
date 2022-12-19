    ! user amplitude subroutine                                                      
      subroutine VUAMP(
     *     ampName, time, ampValueOld, dt, nprops, props, nSvars, 
     *     svars, lFlagsInfo, nSensor, sensorValues, sensorNames,	
     *	    jSensorLookUpTable,
     *     AmpValueNew,
     *     lFlagsDefine,
     *     AmpDerivative, AmpSecDerivative, AmpIncIntegral)

      include 'VABA_PARAM.INC'

    ! time indices
      parameter (iStepTime        = 1,
     *           iTotalTime       = 2,
     *           nTime            = 2)
    ! flags passed in for information
      parameter (iInitialization   = 1,
     *           iRegularInc       = 2,
     *           ikStep            = 3,
     *           nFlagsInfo        = 3)
    ! optional flags to be defined
      parameter (iComputeDeriv     = 1,
     *           iComputeSecDeriv  = 2,
     *           iComputeInteg     = 3,
     *           iStopAnalysis     = 4,
     *           iConcludeStep     = 5,
     *           nFlagsDefine      = 5)
      dimension time(nTime), lFlagsInfo(nFlagsInfo),
     *          lFlagsDefine(nFlagsDefine),
     *          sensorValues(nSensor),
     *          props(nprops),
     *          sVars(nSvars)

      character*80 sensorNames(nSensor)
      character*80 ampName
      dimension jSensorLookUpTable(*)  

! -----------------------------------------------------------------------------------

	  character*256 FILE_ACT, FILE_XM, FILE_XM_OUT
	  
	  real(8) svars
	  real(8) a0, b0, c0, d0, p0, g1, g2, Kse
	  real(8) xm_init, xce_init
	  real(8) A, xce, xm, F, Fc, F_old
	  real(8) xce_r, dxdt
	  real(8) d_xm, d_xce, d_se, xse
	  real(8) gain_length, dt_NEURON

      character*255 jobname,outdir
	  character(len=:), allocatable       :: cwd, cmd, cmd2
	  integer                             :: rc, rc2
	    
! -----------------------------------------------------------------------------------

	  
	  a0 = 2.35			![N]
	  b0 = 24.35		![mm*s-1]
	  c0 = -7.4			![N]
	  d0 = 30.3			![mm*s-1]
	  p0 = 23			![N]
	  g1 = -8			![mm]
	  g2 = 21.4			![mm]
	  Kse = 0.4			![mm-1]
	  xm_init = -8.0	![mm]
	  xce_init = -8		![mm]
	  dt_NEURON = 0.025	![ms]
	  
	  call vgetjobname(jobname,lenjobname)                                         
      call vgetoutdir(outdir,lenoutdir)
	    
	  if (lFlagsInfo(iInitialization).eq.1) then
		 
		! Clear cmd cache, compile NEURON .mod files and run NEURON job
		cwd = outdir(1:lenoutdir)
		cmd = 'ipconfig/flushdns && cd '//trim(outdir)//' && nrnivmodl && python Kim_Model.py'
		rc = system(cmd)
		
		ampValueNew = ampValueOld
		svars(1) = ampValueNew
		svars(2) = 0.0		!Will be used to track ampValueNew that is input back to Abaqus
		svars(3) = 0.0		!Tracker for when to call next NEURON simulation
		svars(10) = 3999.0	!Tracker for reading values in from file
		
		A = 0.0
		xm = xm_init
		F = 0.00001
		svars(13) = xce_init
		
			
	  else
	  
		! After Abaqus has ran for 100ms, call NEURON to run next simulation
		if (svars(3) .eq. 3999) then
			cmd2 = 'ipconfig/flushdns'
			rc = system(cmd2)
			cwd = outdir(1:lenoutdir)
			!cmd = 'ipconfig/flushdns && cd '//trim(outdir)//' && python Kim_Model_restore.py'
			cmd = 'cd '//trim(outdir)//' && python Kim_Model_restore.py'
			rc = system(cmd)
			svars(3) = 0.0
		end if
		
		! Read in activation (mgi) and muscle length (cli) from Module1_2.mod in NEURON
		FILE_ACT=trim(outdir)//'\mgi_output_results.txt'
		OPEN(UNIT=111, FILE=FILE_ACT, STATUS='UNKNOWN', action='READ', access='SEQUENTIAL')

		FILE_XM=trim(outdir)//'\cli_output_results.txt'
		OPEN(UNIT=112, FILE=FILE_XM, STATUS='UNKNOWN', action='READ', access='SEQUENTIAL')
		
		read(111,'(F18.8)') svars(5)	! Activation
		read(112,'(F5.0)') svars(6)	! xm
		
		A = svars(5)
		xm = svars(6)
		
		!! Set initial value of F for the calculation of rate of change of xce
		!!  It should be ampValueOld (previous value of F), unless it was a zero
		!!  because a zero will cause the force to never change from zero
		if (ampValueOld .eq. 0) then
			F_old = 0.00001
		else
			F_old = ampValueOld
		end if
		
		!Calculate muscle force from voltage differential / activation
		g_xm = exp(-((xm-g1)/g2)**2)
		
		Fc = p0*g_xm*A
		
		if (F_old .le. Fc) then
			dxdt = (0.001*(-b0*(Fc-F_old)))/(F_old+(a0*(Fc/p0)))
		else
			gain_length = (-d0*(Fc-F_old))/((2*Fc)-F_old+(c0*Fc/p0))
			if (gain_length .le. 0) then
				dxdt = 100
			else
				dxdt = 0.001*gain_length
			end if
		end if
		
		xce = svars(13) - (dt_NEURON*(-dxdt))
		
		d_xm = xm - xm_init
		d_xce = xce - xce_init
		d_se = d_xm - d_xce
		
		if (d_se .le. 0) then
			xse = 0
		else
			xse = d_se
		end if
		
		F = p0*Kse*xse
		
		svars(2) = F
		ampValueNew = svars(2)

		!! Increase counters
		svars(3) = svars(3) + 1

		svars(10) = svars(10) - 1
		if (svars(10) .eq. 0) then
			! Write muscle length to file to input back into NEURON simulation
			FILE_XM_OUT=trim(outdir)//'\xm_tracker.txt'
			OPEN(UNIT=113, FILE=FILE_XM_OUT, STATUS='UNKNOWN', action='WRITE', access='SEQUENTIAL')
			write(113,*) svars(6)
			close(113)
			
			close(111,status='delete')
			close(112,status='delete')
			svars(10) = 3999
		end if
		
		!Save value of XCE from this step for calculation in next step
		svars(13) = xce
		
	  end if
	  
      return                                                                         
      end                                                                            