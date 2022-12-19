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
!! Define the type of each variable that will be used in the simulation

	  character*256 FILE_F, FILE_F2
	  
	  real(8) svars

      character*255 jobname,outdir
	  character(len=:), allocatable       :: cwd, cmd, cmd2
	  integer                             :: rc, rc2

! -----------------------------------------------------------------------------------
!! Here is what will be ran/calculated each iteration of the simulation
	  
	  ! Get the names of the job and directory to use for file read in/out
	  call vgetjobname(jobname,lenjobname)                                         
      call vgetoutdir(outdir,lenoutdir)	 

	  ! Run this to calculate soleus force amplitude
	  if (ampName(1:11) .eq. 'AMP_SOLEUS3' ) then
	  
		  if (lFlagsInfo(iInitialization).eq.1) then
		  ! Put anything in this 'if' statement that you want to occur only the first time the 
		  !  subroutine is called
			 
			! Call a command window to run the NetPyNE/NEURON simulation from. This runs
			!  (1) a flush of the command window to not have other characters interfere with naming
			!  (2) change directory to navigate to the current working folder
			!  (3) 'nrnivmodl' to compile the necessary dll files for the NEURON .mod files
			!  (4) NetPyNE simulation written in the called .py file
			cwd = outdir(1:lenoutdir)
			cmd = 'ipconfig/flushdns && cd '//trim(outdir)//' && nrnivmodl && python network_model_310MUs.py'
			rc = system(cmd)
			
			! Call a command window to calculate the muscle force from the output results 
			!  from the NetPyNE simulation stored in a .pkl file. This runs
			!  (1) a flush of the command window to not have other characters interfere with naming
			!  (2) change directory to navigate to the current working folder
			!  (3) force calculation written in the called .py file	
			cmd2 = 'ipconfig/flushdns && cd '//trim(outdir)//' && python force_pkl_file.py'
			rc2 = system(cmd2)
			
			! Open the file containing the calculated muscle forces	
			FILE_F=trim(outdir)//'\force_output_results.txt'
			OPEN(UNIT=114, FILE=FILE_F, STATUS='UNKNOWN', action='READ', access='SEQUENTIAL')
			
			! Set the initial value for force [svars(2)]
			ampValueNew = ampValueOld
			svars(1) = ampValueNew
			svars(2) = 0.00001		!Will be used to track ampValueNew (force) that is input back to Abaqus
				
		  else
		  ! Put anything in this 'else' statement that will occur every iteration of the simulation
		  
			! Read in the next force value each iteration of the simulation and set equal to ampValueNew to
			!  be input properly into Abaqus
			read(114,'(F18.6)') svars(2)	!Force 
			ampValueNew = svars(2)
			
		  end if 
	  end if
	  
		! Calculate tibialis anterior force amplitude
		if (ampName(1:11) .eq. 'AMP_TIBANT3' ) then
		
			if (lFlagsInfo(iInitialization).eq.1) then
			! Put anything in this 'if' statement that you want to occur only the first time the 
			!  subroutine is called
				! Open the file containing the calculated muscle forces	
				FILE_F2=trim(outdir)//'\force_output_results_copy.txt'
				OPEN(UNIT=115, FILE=FILE_F2, STATUS='UNKNOWN', action='READ', access='SEQUENTIAL')
				
				! Set the initial value for tibant force [svars(4)]
				ampValueNew = ampValueOld
				svars(3) = ampValueNew
				svars(4) = 0.00001		!Will be used to track ampValueNew (force) that is input back to Abaqus
			else
			! Put anything in this 'else' statement that will occur every iteration of the simulation
			
				! Read in the next force value each iteration of the simulation
				read(115,'(F18.6)') svars(4)	!Force 
				
				! If the soleus force is less than 30N, leave tibant turned off.
				! Otherwise, have tibant force match the soleus force to hold a plantarflexed position.
				if (svars(4) .le. 30) then
					ampValueNew = 0.00001
				else
					ampValueNew = svars(4)
				end if
				
			end if 
		end if 
		

      return                                                                         
      end                                                                            