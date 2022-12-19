## KIM ET AL. MODEL CONVERTED INTO PYTHON FILE FOR USE WITH FORTRAN SUBROUTINE

from neuron import h
h.execute('load_file("nrngui.hoc")')

# Run .hoc files created by Kim et al.
h.execute('load_file("v_e_moto6_export.hoc")')
h.execute('load_file("add_hil_is.hoc")')
h.execute('load_file("add_muscle_unit.hoc")')
h.execute('load_file("mem_mechanism_pass.hoc")')
h.execute('load_file("mem_mechanism_acti.hoc")')
h.execute('load_file("mem_mechanism_muscle.hoc")')
h.execute('load_file("fixnseg.hoc")')
h.execute('load_file("add_pics_istim.hoc")')
h.execute('load_file("Xm.hoc")')

# Check sections created above
#for sec in h.allsec():
#    h.psection(sec=sec)

# Visualize cells created above
#shape_window = h.PlotShape()

# Create recording vectors for output information
v_vec = h.Vector()
v_vec.record(h.soma(0.5)._ref_v)
#d_vec = h.Vector()
#d_vec.record(h.dend[2](0.833)._ref_v)

# Run the full simulation from last state of previous simulation
h.execute('load_file("restore_state.hoc")')
h.run()

# Save the state of the end of the simulation ran
h.execute('load_file("save_state.hoc")')

# Write output voltage to file
volt_list = list(v_vec)
outF = open("voltage_output_results.txt","a+")
for line in volt_list:
    outF.write(str(line))
    outF.write("\n")
outF.close()