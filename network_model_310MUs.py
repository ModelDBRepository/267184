from netpyne import specs, sim

# SCRIPT =======================================================================
netParams = specs.NetParams()

## Population parameters
# Consists of (1) importing each cell from file and (2) creating a population of x number of 
#  cells. In this model, each population only has one cell because we want each motor 
#  neuron to have a unique size. Populations could have more than one cell if there were
#  going to be discrete size levels.
# (Step 2) Create the population for each cell and have them numbered starting from 1
netParams.popParams['Kim_pop_1'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_1'}
netParams.popParams['Kim_pop_2'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_2'}
netParams.popParams['Kim_pop_3'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_3'}
netParams.popParams['Kim_pop_4'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_4'}
netParams.popParams['Kim_pop_5'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_5'}
netParams.popParams['Kim_pop_6'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_6'}
netParams.popParams['Kim_pop_7'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_7'}
netParams.popParams['Kim_pop_8'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_8'}
netParams.popParams['Kim_pop_9'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_9'}
netParams.popParams['Kim_pop_10'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_10'}
netParams.popParams['Kim_pop_11'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_11'}
netParams.popParams['Kim_pop_12'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_12'}
netParams.popParams['Kim_pop_13'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_13'}
netParams.popParams['Kim_pop_14'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_14'}
netParams.popParams['Kim_pop_15'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_15'}
netParams.popParams['Kim_pop_16'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_16'}
netParams.popParams['Kim_pop_17'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_17'}
netParams.popParams['Kim_pop_18'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_18'}
netParams.popParams['Kim_pop_19'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_19'}
netParams.popParams['Kim_pop_20'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_20'}
netParams.popParams['Kim_pop_21'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_21'}
netParams.popParams['Kim_pop_22'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_22'}
netParams.popParams['Kim_pop_23'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_23'}
netParams.popParams['Kim_pop_24'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_24'}
netParams.popParams['Kim_pop_25'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_25'}
netParams.popParams['Kim_pop_26'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_26'}
netParams.popParams['Kim_pop_27'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_27'}
netParams.popParams['Kim_pop_28'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_28'}
netParams.popParams['Kim_pop_29'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_29'}
netParams.popParams['Kim_pop_30'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_30'}
netParams.popParams['Kim_pop_31'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_31'}
netParams.popParams['Kim_pop_32'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_32'}
netParams.popParams['Kim_pop_33'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_33'}
netParams.popParams['Kim_pop_34'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_34'}
netParams.popParams['Kim_pop_35'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_35'}
netParams.popParams['Kim_pop_36'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_36'}
netParams.popParams['Kim_pop_37'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_37'}
netParams.popParams['Kim_pop_38'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_38'}
netParams.popParams['Kim_pop_39'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_39'}
netParams.popParams['Kim_pop_40'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_40'}
netParams.popParams['Kim_pop_41'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_41'}
netParams.popParams['Kim_pop_42'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_42'}
netParams.popParams['Kim_pop_43'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_43'}
netParams.popParams['Kim_pop_44'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_44'}
netParams.popParams['Kim_pop_45'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_45'}
netParams.popParams['Kim_pop_46'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_46'}
netParams.popParams['Kim_pop_47'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_47'}
netParams.popParams['Kim_pop_48'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_48'}
netParams.popParams['Kim_pop_49'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_49'}
netParams.popParams['Kim_pop_50'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_50'}
netParams.popParams['Kim_pop_51'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_51'}
netParams.popParams['Kim_pop_52'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_52'}
netParams.popParams['Kim_pop_53'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_53'}
netParams.popParams['Kim_pop_54'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_54'}
netParams.popParams['Kim_pop_55'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_55'}
netParams.popParams['Kim_pop_56'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_56'}
netParams.popParams['Kim_pop_57'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_57'}
netParams.popParams['Kim_pop_58'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_58'}
netParams.popParams['Kim_pop_59'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_59'}
netParams.popParams['Kim_pop_50'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_50'}
netParams.popParams['Kim_pop_51'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_51'}
netParams.popParams['Kim_pop_52'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_52'}
netParams.popParams['Kim_pop_53'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_53'}
netParams.popParams['Kim_pop_54'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_54'}
netParams.popParams['Kim_pop_55'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_55'}
netParams.popParams['Kim_pop_56'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_56'}
netParams.popParams['Kim_pop_57'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_57'}
netParams.popParams['Kim_pop_58'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_58'}
netParams.popParams['Kim_pop_59'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_59'}
netParams.popParams['Kim_pop_60'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_60'}
netParams.popParams['Kim_pop_61'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_61'}
netParams.popParams['Kim_pop_62'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_62'}
netParams.popParams['Kim_pop_63'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_63'}
netParams.popParams['Kim_pop_64'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_64'}
netParams.popParams['Kim_pop_65'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_65'}
netParams.popParams['Kim_pop_66'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_66'}
netParams.popParams['Kim_pop_67'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_67'}
netParams.popParams['Kim_pop_68'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_68'}
netParams.popParams['Kim_pop_69'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_69'}
netParams.popParams['Kim_pop_70'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_70'}
netParams.popParams['Kim_pop_71'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_71'}
netParams.popParams['Kim_pop_72'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_72'}
netParams.popParams['Kim_pop_73'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_73'}
netParams.popParams['Kim_pop_74'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_74'}
netParams.popParams['Kim_pop_75'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_75'}
netParams.popParams['Kim_pop_76'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_76'}
netParams.popParams['Kim_pop_77'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_77'}
netParams.popParams['Kim_pop_78'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_78'}
netParams.popParams['Kim_pop_79'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_79'}
netParams.popParams['Kim_pop_80'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_80'}
netParams.popParams['Kim_pop_81'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_81'}
netParams.popParams['Kim_pop_82'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_82'}
netParams.popParams['Kim_pop_83'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_83'}
netParams.popParams['Kim_pop_84'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_84'}
netParams.popParams['Kim_pop_85'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_85'}
netParams.popParams['Kim_pop_86'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_86'}
netParams.popParams['Kim_pop_87'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_87'}
netParams.popParams['Kim_pop_88'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_88'}
netParams.popParams['Kim_pop_89'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_89'}
netParams.popParams['Kim_pop_90'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_90'}
netParams.popParams['Kim_pop_91'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_91'}
netParams.popParams['Kim_pop_92'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_92'}
netParams.popParams['Kim_pop_93'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_93'}
netParams.popParams['Kim_pop_94'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_94'}
netParams.popParams['Kim_pop_95'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_95'}
netParams.popParams['Kim_pop_96'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_96'}
netParams.popParams['Kim_pop_97'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_97'}
netParams.popParams['Kim_pop_98'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_98'}
netParams.popParams['Kim_pop_99'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_99'}
netParams.popParams['Kim_pop_100'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_100'}
netParams.popParams['Kim_pop_101'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_101'}
netParams.popParams['Kim_pop_102'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_102'}
netParams.popParams['Kim_pop_103'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_103'}
netParams.popParams['Kim_pop_104'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_104'}
netParams.popParams['Kim_pop_105'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_105'}
netParams.popParams['Kim_pop_106'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_106'}
netParams.popParams['Kim_pop_107'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_107'}
netParams.popParams['Kim_pop_108'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_108'}
netParams.popParams['Kim_pop_109'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_109'}
netParams.popParams['Kim_pop_110'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_110'}
netParams.popParams['Kim_pop_111'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_111'}
netParams.popParams['Kim_pop_112'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_112'}
netParams.popParams['Kim_pop_113'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_113'}
netParams.popParams['Kim_pop_114'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_114'}
netParams.popParams['Kim_pop_115'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_115'}
netParams.popParams['Kim_pop_116'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_116'}
netParams.popParams['Kim_pop_117'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_117'}
netParams.popParams['Kim_pop_118'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_118'}
netParams.popParams['Kim_pop_119'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_119'}
netParams.popParams['Kim_pop_120'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_120'}
netParams.popParams['Kim_pop_121'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_121'}
netParams.popParams['Kim_pop_122'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_122'}
netParams.popParams['Kim_pop_123'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_123'}
netParams.popParams['Kim_pop_124'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_124'}
netParams.popParams['Kim_pop_125'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_125'}
netParams.popParams['Kim_pop_126'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_126'}
netParams.popParams['Kim_pop_127'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_127'}
netParams.popParams['Kim_pop_128'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_128'}
netParams.popParams['Kim_pop_129'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_129'}
netParams.popParams['Kim_pop_130'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_130'}
netParams.popParams['Kim_pop_131'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_131'}
netParams.popParams['Kim_pop_132'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_132'}
netParams.popParams['Kim_pop_133'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_133'}
netParams.popParams['Kim_pop_134'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_134'}
netParams.popParams['Kim_pop_135'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_135'}
netParams.popParams['Kim_pop_136'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_136'}
netParams.popParams['Kim_pop_137'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_137'}
netParams.popParams['Kim_pop_138'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_138'}
netParams.popParams['Kim_pop_139'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_139'}
netParams.popParams['Kim_pop_140'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_140'}
netParams.popParams['Kim_pop_141'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_141'}
netParams.popParams['Kim_pop_142'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_142'}
netParams.popParams['Kim_pop_143'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_143'}
netParams.popParams['Kim_pop_144'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_144'}
netParams.popParams['Kim_pop_145'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_145'}
netParams.popParams['Kim_pop_146'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_146'}
netParams.popParams['Kim_pop_147'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_147'}
netParams.popParams['Kim_pop_148'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_148'}
netParams.popParams['Kim_pop_149'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_149'}
netParams.popParams['Kim_pop_150'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_150'}
netParams.popParams['Kim_pop_151'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_151'}
netParams.popParams['Kim_pop_152'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_152'}
netParams.popParams['Kim_pop_153'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_153'}
netParams.popParams['Kim_pop_154'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_154'}
netParams.popParams['Kim_pop_155'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_155'}
netParams.popParams['Kim_pop_156'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_156'}
netParams.popParams['Kim_pop_157'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_157'}
netParams.popParams['Kim_pop_158'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_158'}
netParams.popParams['Kim_pop_159'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_159'}
netParams.popParams['Kim_pop_160'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_160'}
netParams.popParams['Kim_pop_161'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_161'}
netParams.popParams['Kim_pop_162'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_162'}
netParams.popParams['Kim_pop_163'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_163'}
netParams.popParams['Kim_pop_164'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_164'}
netParams.popParams['Kim_pop_165'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_165'}
netParams.popParams['Kim_pop_166'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_166'}
netParams.popParams['Kim_pop_167'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_167'}
netParams.popParams['Kim_pop_168'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_168'}
netParams.popParams['Kim_pop_169'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_169'}
netParams.popParams['Kim_pop_170'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_170'}
netParams.popParams['Kim_pop_171'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_171'}
netParams.popParams['Kim_pop_172'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_172'}
netParams.popParams['Kim_pop_173'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_173'}
netParams.popParams['Kim_pop_174'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_174'}
netParams.popParams['Kim_pop_175'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_175'}
netParams.popParams['Kim_pop_176'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_176'}
netParams.popParams['Kim_pop_177'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_177'}
netParams.popParams['Kim_pop_178'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_178'}
netParams.popParams['Kim_pop_179'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_179'}
netParams.popParams['Kim_pop_180'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_180'}
netParams.popParams['Kim_pop_181'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_181'}
netParams.popParams['Kim_pop_182'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_182'}
netParams.popParams['Kim_pop_183'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_183'}
netParams.popParams['Kim_pop_184'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_184'}
netParams.popParams['Kim_pop_185'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_185'}
netParams.popParams['Kim_pop_186'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_186'}
netParams.popParams['Kim_pop_187'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_187'}
netParams.popParams['Kim_pop_188'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_188'}
netParams.popParams['Kim_pop_189'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_189'}
netParams.popParams['Kim_pop_190'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_190'}
netParams.popParams['Kim_pop_191'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_191'}
netParams.popParams['Kim_pop_192'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_192'}
netParams.popParams['Kim_pop_193'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_193'}
netParams.popParams['Kim_pop_194'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_194'}
netParams.popParams['Kim_pop_195'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_195'}
netParams.popParams['Kim_pop_196'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_196'}
netParams.popParams['Kim_pop_197'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_197'}
netParams.popParams['Kim_pop_198'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_198'}
netParams.popParams['Kim_pop_199'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_199'}
netParams.popParams['Kim_pop_200'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_200'}
netParams.popParams['Kim_pop_201'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_201'}
netParams.popParams['Kim_pop_202'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_202'}
netParams.popParams['Kim_pop_203'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_203'}
netParams.popParams['Kim_pop_204'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_204'}
netParams.popParams['Kim_pop_205'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_205'}
netParams.popParams['Kim_pop_206'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_206'}
netParams.popParams['Kim_pop_207'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_207'}
netParams.popParams['Kim_pop_208'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_208'}
netParams.popParams['Kim_pop_209'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_209'}
netParams.popParams['Kim_pop_210'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_210'}
netParams.popParams['Kim_pop_211'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_211'}
netParams.popParams['Kim_pop_212'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_212'}
netParams.popParams['Kim_pop_213'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_213'}
netParams.popParams['Kim_pop_214'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_214'}
netParams.popParams['Kim_pop_215'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_215'}
netParams.popParams['Kim_pop_216'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_216'}
netParams.popParams['Kim_pop_217'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_217'}
netParams.popParams['Kim_pop_218'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_218'}
netParams.popParams['Kim_pop_219'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_219'}
netParams.popParams['Kim_pop_220'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_220'}
netParams.popParams['Kim_pop_221'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_221'}
netParams.popParams['Kim_pop_222'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_222'}
netParams.popParams['Kim_pop_223'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_223'}
netParams.popParams['Kim_pop_224'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_224'}
netParams.popParams['Kim_pop_225'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_225'}
netParams.popParams['Kim_pop_226'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_226'}
netParams.popParams['Kim_pop_227'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_227'}
netParams.popParams['Kim_pop_228'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_228'}
netParams.popParams['Kim_pop_229'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_229'}
netParams.popParams['Kim_pop_230'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_230'}
netParams.popParams['Kim_pop_231'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_231'}
netParams.popParams['Kim_pop_232'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_232'}
netParams.popParams['Kim_pop_233'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_233'}
netParams.popParams['Kim_pop_234'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_234'}
netParams.popParams['Kim_pop_235'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_235'}
netParams.popParams['Kim_pop_236'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_236'}
netParams.popParams['Kim_pop_237'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_237'}
netParams.popParams['Kim_pop_238'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_238'}
netParams.popParams['Kim_pop_239'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_239'}
netParams.popParams['Kim_pop_240'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_240'}
netParams.popParams['Kim_pop_241'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_241'}
netParams.popParams['Kim_pop_242'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_242'}
netParams.popParams['Kim_pop_243'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_243'}
netParams.popParams['Kim_pop_244'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_244'}
netParams.popParams['Kim_pop_245'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_245'}
netParams.popParams['Kim_pop_246'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_246'}
netParams.popParams['Kim_pop_247'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_247'}
netParams.popParams['Kim_pop_248'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_248'}
netParams.popParams['Kim_pop_249'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_249'}
netParams.popParams['Kim_pop_250'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_250'}
netParams.popParams['Kim_pop_251'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_251'}
netParams.popParams['Kim_pop_252'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_252'}
netParams.popParams['Kim_pop_253'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_253'}
netParams.popParams['Kim_pop_254'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_254'}
netParams.popParams['Kim_pop_255'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_255'}
netParams.popParams['Kim_pop_256'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_256'}
netParams.popParams['Kim_pop_257'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_257'}
netParams.popParams['Kim_pop_258'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_258'}
netParams.popParams['Kim_pop_259'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_259'}
netParams.popParams['Kim_pop_260'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_260'}
netParams.popParams['Kim_pop_261'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_261'}
netParams.popParams['Kim_pop_262'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_262'}
netParams.popParams['Kim_pop_263'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_263'}
netParams.popParams['Kim_pop_264'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_264'}
netParams.popParams['Kim_pop_265'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_265'}
netParams.popParams['Kim_pop_266'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_266'}
netParams.popParams['Kim_pop_267'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_267'}
netParams.popParams['Kim_pop_268'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_268'}
netParams.popParams['Kim_pop_269'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_269'}
netParams.popParams['Kim_pop_270'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_270'}
netParams.popParams['Kim_pop_271'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_271'}
netParams.popParams['Kim_pop_272'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_272'}
netParams.popParams['Kim_pop_273'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_273'}
netParams.popParams['Kim_pop_274'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_274'}
netParams.popParams['Kim_pop_275'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_275'}
netParams.popParams['Kim_pop_276'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_276'}
netParams.popParams['Kim_pop_277'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_277'}
netParams.popParams['Kim_pop_278'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_278'}
netParams.popParams['Kim_pop_279'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_279'}
netParams.popParams['Kim_pop_280'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_280'}
netParams.popParams['Kim_pop_281'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_281'}
netParams.popParams['Kim_pop_282'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_282'}
netParams.popParams['Kim_pop_283'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_283'}
netParams.popParams['Kim_pop_284'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_284'}
netParams.popParams['Kim_pop_285'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_285'}
netParams.popParams['Kim_pop_286'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_286'}
netParams.popParams['Kim_pop_287'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_287'}
netParams.popParams['Kim_pop_288'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_288'}
netParams.popParams['Kim_pop_289'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_289'}
netParams.popParams['Kim_pop_290'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_290'}
netParams.popParams['Kim_pop_291'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_291'}
netParams.popParams['Kim_pop_292'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_292'}
netParams.popParams['Kim_pop_293'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_293'}
netParams.popParams['Kim_pop_294'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_294'}
netParams.popParams['Kim_pop_295'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_295'}
netParams.popParams['Kim_pop_296'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_296'}
netParams.popParams['Kim_pop_297'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_297'}
netParams.popParams['Kim_pop_298'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_298'}
netParams.popParams['Kim_pop_299'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_299'}
netParams.popParams['Kim_pop_300'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_300'}
netParams.popParams['Kim_pop_301'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_301'}
netParams.popParams['Kim_pop_302'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_302'}
netParams.popParams['Kim_pop_303'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_303'}
netParams.popParams['Kim_pop_304'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_304'}
netParams.popParams['Kim_pop_305'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_305'}
netParams.popParams['Kim_pop_306'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_306'}
netParams.popParams['Kim_pop_307'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_307'}
netParams.popParams['Kim_pop_308'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_308'}
netParams.popParams['Kim_pop_309'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_309'}
netParams.popParams['Kim_pop_310'] = {'cellType': 'MU', 'numCells': 1, 'cellModel': 'Kim_310'}

# (Step 1) Import each cell from file including geometry and properties. somaAtOrigin must be set to 
#  False otherwise each newly imported cell will override the previous one.
cellRule = netParams.importCellParams(label='motor_unit_1', conds={'cellType': 'MU', 'cellModel': 'Kim_1'}, 
	fileName='motor_unit_template_1.hoc', cellName='motor_unit_1', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_2', conds={'cellType': 'MU', 'cellModel': 'Kim_2'}, 
	fileName='motor_unit_template_2.hoc', cellName='motor_unit_2', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_3', conds={'cellType': 'MU', 'cellModel': 'Kim_3'}, 
	fileName='motor_unit_template_3.hoc', cellName='motor_unit_3', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_4', conds={'cellType': 'MU', 'cellModel': 'Kim_4'}, 
	fileName='motor_unit_template_4.hoc', cellName='motor_unit_4', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_5', conds={'cellType': 'MU', 'cellModel': 'Kim_5'}, 
	fileName='motor_unit_template_5.hoc', cellName='motor_unit_5', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_6', conds={'cellType': 'MU', 'cellModel': 'Kim_6'}, 
	fileName='motor_unit_template_6.hoc', cellName='motor_unit_6', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_7', conds={'cellType': 'MU', 'cellModel': 'Kim_7'}, 
	fileName='motor_unit_template_7.hoc', cellName='motor_unit_7', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_8', conds={'cellType': 'MU', 'cellModel': 'Kim_8'}, 
	fileName='motor_unit_template_8.hoc', cellName='motor_unit_8', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_9', conds={'cellType': 'MU', 'cellModel': 'Kim_9'}, 
	fileName='motor_unit_template_9.hoc', cellName='motor_unit_9', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_10', conds={'cellType': 'MU', 'cellModel': 'Kim_10'}, 
	fileName='motor_unit_template_10.hoc', cellName='motor_unit_10', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_11', conds={'cellType': 'MU', 'cellModel': 'Kim_11'}, 
	fileName='motor_unit_template_11.hoc', cellName='motor_unit_11', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_12', conds={'cellType': 'MU', 'cellModel': 'Kim_12'}, 
	fileName='motor_unit_template_12.hoc', cellName='motor_unit_12', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_13', conds={'cellType': 'MU', 'cellModel': 'Kim_13'}, 
	fileName='motor_unit_template_13.hoc', cellName='motor_unit_13', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_14', conds={'cellType': 'MU', 'cellModel': 'Kim_14'}, 
	fileName='motor_unit_template_14.hoc', cellName='motor_unit_14', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_15', conds={'cellType': 'MU', 'cellModel': 'Kim_15'}, 
	fileName='motor_unit_template_15.hoc', cellName='motor_unit_15', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_16', conds={'cellType': 'MU', 'cellModel': 'Kim_16'}, 
	fileName='motor_unit_template_16.hoc', cellName='motor_unit_16', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_17', conds={'cellType': 'MU', 'cellModel': 'Kim_17'}, 
	fileName='motor_unit_template_17.hoc', cellName='motor_unit_17', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_18', conds={'cellType': 'MU', 'cellModel': 'Kim_18'}, 
	fileName='motor_unit_template_18.hoc', cellName='motor_unit_18', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_19', conds={'cellType': 'MU', 'cellModel': 'Kim_19'}, 
	fileName='motor_unit_template_19.hoc', cellName='motor_unit_19', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_20', conds={'cellType': 'MU', 'cellModel': 'Kim_20'}, 
	fileName='motor_unit_template_20.hoc', cellName='motor_unit_20', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_21', conds={'cellType': 'MU', 'cellModel': 'Kim_21'}, 
	fileName='motor_unit_template_21.hoc', cellName='motor_unit_21', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_22', conds={'cellType': 'MU', 'cellModel': 'Kim_22'}, 
	fileName='motor_unit_template_22.hoc', cellName='motor_unit_22', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_23', conds={'cellType': 'MU', 'cellModel': 'Kim_23'}, 
	fileName='motor_unit_template_23.hoc', cellName='motor_unit_23', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_24', conds={'cellType': 'MU', 'cellModel': 'Kim_24'}, 
	fileName='motor_unit_template_24.hoc', cellName='motor_unit_24', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_25', conds={'cellType': 'MU', 'cellModel': 'Kim_25'}, 
	fileName='motor_unit_template_25.hoc', cellName='motor_unit_25', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_26', conds={'cellType': 'MU', 'cellModel': 'Kim_26'}, 
	fileName='motor_unit_template_26.hoc', cellName='motor_unit_26', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_27', conds={'cellType': 'MU', 'cellModel': 'Kim_27'}, 
	fileName='motor_unit_template_27.hoc', cellName='motor_unit_27', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_28', conds={'cellType': 'MU', 'cellModel': 'Kim_28'}, 
	fileName='motor_unit_template_28.hoc', cellName='motor_unit_28', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_29', conds={'cellType': 'MU', 'cellModel': 'Kim_29'}, 
	fileName='motor_unit_template_29.hoc', cellName='motor_unit_29', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_30', conds={'cellType': 'MU', 'cellModel': 'Kim_30'}, 
	fileName='motor_unit_template_30.hoc', cellName='motor_unit_30', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_31', conds={'cellType': 'MU', 'cellModel': 'Kim_31'}, 
	fileName='motor_unit_template_31.hoc', cellName='motor_unit_31', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_32', conds={'cellType': 'MU', 'cellModel': 'Kim_32'}, 
	fileName='motor_unit_template_32.hoc', cellName='motor_unit_32', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_33', conds={'cellType': 'MU', 'cellModel': 'Kim_33'}, 
	fileName='motor_unit_template_33.hoc', cellName='motor_unit_33', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_34', conds={'cellType': 'MU', 'cellModel': 'Kim_34'}, 
	fileName='motor_unit_template_34.hoc', cellName='motor_unit_34', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_35', conds={'cellType': 'MU', 'cellModel': 'Kim_35'}, 
	fileName='motor_unit_template_35.hoc', cellName='motor_unit_35', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_36', conds={'cellType': 'MU', 'cellModel': 'Kim_36'}, 
	fileName='motor_unit_template_36.hoc', cellName='motor_unit_36', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_37', conds={'cellType': 'MU', 'cellModel': 'Kim_37'}, 
	fileName='motor_unit_template_37.hoc', cellName='motor_unit_37', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_38', conds={'cellType': 'MU', 'cellModel': 'Kim_38'}, 
	fileName='motor_unit_template_38.hoc', cellName='motor_unit_38', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_39', conds={'cellType': 'MU', 'cellModel': 'Kim_39'}, 
	fileName='motor_unit_template_39.hoc', cellName='motor_unit_39', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_40', conds={'cellType': 'MU', 'cellModel': 'Kim_40'}, 
	fileName='motor_unit_template_40.hoc', cellName='motor_unit_40', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_41', conds={'cellType': 'MU', 'cellModel': 'Kim_41'}, 
	fileName='motor_unit_template_41.hoc', cellName='motor_unit_41', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_42', conds={'cellType': 'MU', 'cellModel': 'Kim_42'}, 
	fileName='motor_unit_template_42.hoc', cellName='motor_unit_42', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_43', conds={'cellType': 'MU', 'cellModel': 'Kim_43'}, 
	fileName='motor_unit_template_43.hoc', cellName='motor_unit_43', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_44', conds={'cellType': 'MU', 'cellModel': 'Kim_44'}, 
	fileName='motor_unit_template_44.hoc', cellName='motor_unit_44', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_45', conds={'cellType': 'MU', 'cellModel': 'Kim_45'}, 
	fileName='motor_unit_template_45.hoc', cellName='motor_unit_45', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_46', conds={'cellType': 'MU', 'cellModel': 'Kim_46'}, 
	fileName='motor_unit_template_46.hoc', cellName='motor_unit_46', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_47', conds={'cellType': 'MU', 'cellModel': 'Kim_47'}, 
	fileName='motor_unit_template_47.hoc', cellName='motor_unit_47', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_48', conds={'cellType': 'MU', 'cellModel': 'Kim_48'}, 
	fileName='motor_unit_template_48.hoc', cellName='motor_unit_48', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_49', conds={'cellType': 'MU', 'cellModel': 'Kim_49'}, 
	fileName='motor_unit_template_49.hoc', cellName='motor_unit_49', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_50', conds={'cellType': 'MU', 'cellModel': 'Kim_50'}, 
	fileName='motor_unit_template_50.hoc', cellName='motor_unit_50', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_51', conds={'cellType': 'MU', 'cellModel': 'Kim_51'}, 
	fileName='motor_unit_template_51.hoc', cellName='motor_unit_51', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_52', conds={'cellType': 'MU', 'cellModel': 'Kim_52'}, 
	fileName='motor_unit_template_52.hoc', cellName='motor_unit_52', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_53', conds={'cellType': 'MU', 'cellModel': 'Kim_53'}, 
	fileName='motor_unit_template_53.hoc', cellName='motor_unit_53', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_54', conds={'cellType': 'MU', 'cellModel': 'Kim_54'}, 
	fileName='motor_unit_template_54.hoc', cellName='motor_unit_54', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_55', conds={'cellType': 'MU', 'cellModel': 'Kim_55'}, 
	fileName='motor_unit_template_55.hoc', cellName='motor_unit_55', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_56', conds={'cellType': 'MU', 'cellModel': 'Kim_56'}, 
	fileName='motor_unit_template_56.hoc', cellName='motor_unit_56', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_57', conds={'cellType': 'MU', 'cellModel': 'Kim_57'}, 
	fileName='motor_unit_template_57.hoc', cellName='motor_unit_57', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_58', conds={'cellType': 'MU', 'cellModel': 'Kim_58'}, 
	fileName='motor_unit_template_58.hoc', cellName='motor_unit_58', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_59', conds={'cellType': 'MU', 'cellModel': 'Kim_59'}, 
	fileName='motor_unit_template_59.hoc', cellName='motor_unit_59', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_60', conds={'cellType': 'MU', 'cellModel': 'Kim_60'}, 
	fileName='motor_unit_template_60.hoc', cellName='motor_unit_60', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_61', conds={'cellType': 'MU', 'cellModel': 'Kim_61'}, 
	fileName='motor_unit_template_61.hoc', cellName='motor_unit_61', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_62', conds={'cellType': 'MU', 'cellModel': 'Kim_62'}, 
	fileName='motor_unit_template_62.hoc', cellName='motor_unit_62', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_63', conds={'cellType': 'MU', 'cellModel': 'Kim_63'}, 
	fileName='motor_unit_template_63.hoc', cellName='motor_unit_63', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_64', conds={'cellType': 'MU', 'cellModel': 'Kim_64'}, 
	fileName='motor_unit_template_64.hoc', cellName='motor_unit_64', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_65', conds={'cellType': 'MU', 'cellModel': 'Kim_65'}, 
	fileName='motor_unit_template_65.hoc', cellName='motor_unit_65', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_66', conds={'cellType': 'MU', 'cellModel': 'Kim_66'}, 
	fileName='motor_unit_template_66.hoc', cellName='motor_unit_66', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_67', conds={'cellType': 'MU', 'cellModel': 'Kim_67'}, 
	fileName='motor_unit_template_67.hoc', cellName='motor_unit_67', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_68', conds={'cellType': 'MU', 'cellModel': 'Kim_68'}, 
	fileName='motor_unit_template_68.hoc', cellName='motor_unit_68', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_69', conds={'cellType': 'MU', 'cellModel': 'Kim_69'}, 
	fileName='motor_unit_template_69.hoc', cellName='motor_unit_69', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_70', conds={'cellType': 'MU', 'cellModel': 'Kim_70'}, 
	fileName='motor_unit_template_70.hoc', cellName='motor_unit_70', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_71', conds={'cellType': 'MU', 'cellModel': 'Kim_71'}, 
	fileName='motor_unit_template_71.hoc', cellName='motor_unit_71', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_72', conds={'cellType': 'MU', 'cellModel': 'Kim_72'}, 
	fileName='motor_unit_template_72.hoc', cellName='motor_unit_72', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_73', conds={'cellType': 'MU', 'cellModel': 'Kim_73'}, 
	fileName='motor_unit_template_73.hoc', cellName='motor_unit_73', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_74', conds={'cellType': 'MU', 'cellModel': 'Kim_74'}, 
	fileName='motor_unit_template_74.hoc', cellName='motor_unit_74', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_75', conds={'cellType': 'MU', 'cellModel': 'Kim_75'}, 
	fileName='motor_unit_template_75.hoc', cellName='motor_unit_75', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_76', conds={'cellType': 'MU', 'cellModel': 'Kim_76'}, 
	fileName='motor_unit_template_76.hoc', cellName='motor_unit_76', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_77', conds={'cellType': 'MU', 'cellModel': 'Kim_77'}, 
	fileName='motor_unit_template_77.hoc', cellName='motor_unit_77', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_78', conds={'cellType': 'MU', 'cellModel': 'Kim_78'}, 
	fileName='motor_unit_template_78.hoc', cellName='motor_unit_78', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_79', conds={'cellType': 'MU', 'cellModel': 'Kim_79'}, 
	fileName='motor_unit_template_79.hoc', cellName='motor_unit_79', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_80', conds={'cellType': 'MU', 'cellModel': 'Kim_80'}, 
	fileName='motor_unit_template_80.hoc', cellName='motor_unit_80', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_81', conds={'cellType': 'MU', 'cellModel': 'Kim_81'}, 
	fileName='motor_unit_template_81.hoc', cellName='motor_unit_81', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_82', conds={'cellType': 'MU', 'cellModel': 'Kim_82'}, 
	fileName='motor_unit_template_82.hoc', cellName='motor_unit_82', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_83', conds={'cellType': 'MU', 'cellModel': 'Kim_83'}, 
	fileName='motor_unit_template_83.hoc', cellName='motor_unit_83', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_84', conds={'cellType': 'MU', 'cellModel': 'Kim_84'}, 
	fileName='motor_unit_template_84.hoc', cellName='motor_unit_84', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_85', conds={'cellType': 'MU', 'cellModel': 'Kim_85'}, 
	fileName='motor_unit_template_85.hoc', cellName='motor_unit_85', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_86', conds={'cellType': 'MU', 'cellModel': 'Kim_86'}, 
	fileName='motor_unit_template_86.hoc', cellName='motor_unit_86', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_87', conds={'cellType': 'MU', 'cellModel': 'Kim_87'}, 
	fileName='motor_unit_template_87.hoc', cellName='motor_unit_87', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_88', conds={'cellType': 'MU', 'cellModel': 'Kim_88'}, 
	fileName='motor_unit_template_88.hoc', cellName='motor_unit_88', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_89', conds={'cellType': 'MU', 'cellModel': 'Kim_89'}, 
	fileName='motor_unit_template_89.hoc', cellName='motor_unit_89', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_90', conds={'cellType': 'MU', 'cellModel': 'Kim_90'}, 
	fileName='motor_unit_template_90.hoc', cellName='motor_unit_90', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_91', conds={'cellType': 'MU', 'cellModel': 'Kim_91'}, 
	fileName='motor_unit_template_91.hoc', cellName='motor_unit_91', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_92', conds={'cellType': 'MU', 'cellModel': 'Kim_92'}, 
	fileName='motor_unit_template_92.hoc', cellName='motor_unit_92', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_93', conds={'cellType': 'MU', 'cellModel': 'Kim_93'}, 
	fileName='motor_unit_template_93.hoc', cellName='motor_unit_93', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_94', conds={'cellType': 'MU', 'cellModel': 'Kim_94'}, 
	fileName='motor_unit_template_94.hoc', cellName='motor_unit_94', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_95', conds={'cellType': 'MU', 'cellModel': 'Kim_95'}, 
	fileName='motor_unit_template_95.hoc', cellName='motor_unit_95', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_96', conds={'cellType': 'MU', 'cellModel': 'Kim_96'}, 
	fileName='motor_unit_template_96.hoc', cellName='motor_unit_96', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_97', conds={'cellType': 'MU', 'cellModel': 'Kim_97'}, 
	fileName='motor_unit_template_97.hoc', cellName='motor_unit_97', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_98', conds={'cellType': 'MU', 'cellModel': 'Kim_98'}, 
	fileName='motor_unit_template_98.hoc', cellName='motor_unit_98', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_99', conds={'cellType': 'MU', 'cellModel': 'Kim_99'}, 
	fileName='motor_unit_template_99.hoc', cellName='motor_unit_99', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_100', conds={'cellType': 'MU', 'cellModel': 'Kim_100'}, 
	fileName='motor_unit_template_100.hoc', cellName='motor_unit_100', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_101', conds={'cellType': 'MU', 'cellModel': 'Kim_101'}, 
	fileName='motor_unit_template_101.hoc', cellName='motor_unit_101', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_102', conds={'cellType': 'MU', 'cellModel': 'Kim_102'}, 
	fileName='motor_unit_template_102.hoc', cellName='motor_unit_102', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_103', conds={'cellType': 'MU', 'cellModel': 'Kim_103'}, 
	fileName='motor_unit_template_103.hoc', cellName='motor_unit_103', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_104', conds={'cellType': 'MU', 'cellModel': 'Kim_104'}, 
	fileName='motor_unit_template_104.hoc', cellName='motor_unit_104', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_105', conds={'cellType': 'MU', 'cellModel': 'Kim_105'}, 
	fileName='motor_unit_template_105.hoc', cellName='motor_unit_105', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_106', conds={'cellType': 'MU', 'cellModel': 'Kim_106'}, 
	fileName='motor_unit_template_106.hoc', cellName='motor_unit_106', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_107', conds={'cellType': 'MU', 'cellModel': 'Kim_107'}, 
	fileName='motor_unit_template_107.hoc', cellName='motor_unit_107', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_108', conds={'cellType': 'MU', 'cellModel': 'Kim_108'}, 
	fileName='motor_unit_template_108.hoc', cellName='motor_unit_108', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_109', conds={'cellType': 'MU', 'cellModel': 'Kim_109'}, 
	fileName='motor_unit_template_109.hoc', cellName='motor_unit_109', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_110', conds={'cellType': 'MU', 'cellModel': 'Kim_110'}, 
	fileName='motor_unit_template_110.hoc', cellName='motor_unit_110', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_111', conds={'cellType': 'MU', 'cellModel': 'Kim_111'}, 
	fileName='motor_unit_template_111.hoc', cellName='motor_unit_111', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_112', conds={'cellType': 'MU', 'cellModel': 'Kim_112'}, 
	fileName='motor_unit_template_112.hoc', cellName='motor_unit_112', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_113', conds={'cellType': 'MU', 'cellModel': 'Kim_113'}, 
	fileName='motor_unit_template_113.hoc', cellName='motor_unit_113', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_114', conds={'cellType': 'MU', 'cellModel': 'Kim_114'}, 
	fileName='motor_unit_template_114.hoc', cellName='motor_unit_114', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_115', conds={'cellType': 'MU', 'cellModel': 'Kim_115'}, 
	fileName='motor_unit_template_115.hoc', cellName='motor_unit_115', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_116', conds={'cellType': 'MU', 'cellModel': 'Kim_116'}, 
	fileName='motor_unit_template_116.hoc', cellName='motor_unit_116', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_117', conds={'cellType': 'MU', 'cellModel': 'Kim_117'}, 
	fileName='motor_unit_template_117.hoc', cellName='motor_unit_117', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_118', conds={'cellType': 'MU', 'cellModel': 'Kim_118'}, 
	fileName='motor_unit_template_118.hoc', cellName='motor_unit_118', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_119', conds={'cellType': 'MU', 'cellModel': 'Kim_119'}, 
	fileName='motor_unit_template_119.hoc', cellName='motor_unit_119', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_120', conds={'cellType': 'MU', 'cellModel': 'Kim_120'}, 
	fileName='motor_unit_template_120.hoc', cellName='motor_unit_120', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_121', conds={'cellType': 'MU', 'cellModel': 'Kim_121'}, 
	fileName='motor_unit_template_121.hoc', cellName='motor_unit_121', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_122', conds={'cellType': 'MU', 'cellModel': 'Kim_122'}, 
	fileName='motor_unit_template_122.hoc', cellName='motor_unit_122', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_123', conds={'cellType': 'MU', 'cellModel': 'Kim_123'}, 
	fileName='motor_unit_template_123.hoc', cellName='motor_unit_123', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_124', conds={'cellType': 'MU', 'cellModel': 'Kim_124'}, 
	fileName='motor_unit_template_124.hoc', cellName='motor_unit_124', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_125', conds={'cellType': 'MU', 'cellModel': 'Kim_125'}, 
	fileName='motor_unit_template_125.hoc', cellName='motor_unit_125', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_126', conds={'cellType': 'MU', 'cellModel': 'Kim_126'}, 
	fileName='motor_unit_template_126.hoc', cellName='motor_unit_126', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_127', conds={'cellType': 'MU', 'cellModel': 'Kim_127'}, 
	fileName='motor_unit_template_127.hoc', cellName='motor_unit_127', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_128', conds={'cellType': 'MU', 'cellModel': 'Kim_128'}, 
	fileName='motor_unit_template_128.hoc', cellName='motor_unit_128', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_129', conds={'cellType': 'MU', 'cellModel': 'Kim_129'}, 
	fileName='motor_unit_template_129.hoc', cellName='motor_unit_129', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_130', conds={'cellType': 'MU', 'cellModel': 'Kim_130'}, 
	fileName='motor_unit_template_130.hoc', cellName='motor_unit_130', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_131', conds={'cellType': 'MU', 'cellModel': 'Kim_131'}, 
	fileName='motor_unit_template_131.hoc', cellName='motor_unit_131', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_132', conds={'cellType': 'MU', 'cellModel': 'Kim_132'}, 
	fileName='motor_unit_template_132.hoc', cellName='motor_unit_132', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_133', conds={'cellType': 'MU', 'cellModel': 'Kim_133'}, 
	fileName='motor_unit_template_133.hoc', cellName='motor_unit_133', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_134', conds={'cellType': 'MU', 'cellModel': 'Kim_134'}, 
	fileName='motor_unit_template_134.hoc', cellName='motor_unit_134', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_135', conds={'cellType': 'MU', 'cellModel': 'Kim_135'}, 
	fileName='motor_unit_template_135.hoc', cellName='motor_unit_135', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_136', conds={'cellType': 'MU', 'cellModel': 'Kim_136'}, 
	fileName='motor_unit_template_136.hoc', cellName='motor_unit_136', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_137', conds={'cellType': 'MU', 'cellModel': 'Kim_137'}, 
	fileName='motor_unit_template_137.hoc', cellName='motor_unit_137', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_138', conds={'cellType': 'MU', 'cellModel': 'Kim_138'}, 
	fileName='motor_unit_template_138.hoc', cellName='motor_unit_138', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_139', conds={'cellType': 'MU', 'cellModel': 'Kim_139'}, 
	fileName='motor_unit_template_139.hoc', cellName='motor_unit_139', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_140', conds={'cellType': 'MU', 'cellModel': 'Kim_140'}, 
	fileName='motor_unit_template_140.hoc', cellName='motor_unit_140', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_141', conds={'cellType': 'MU', 'cellModel': 'Kim_141'}, 
	fileName='motor_unit_template_141.hoc', cellName='motor_unit_141', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_142', conds={'cellType': 'MU', 'cellModel': 'Kim_142'}, 
	fileName='motor_unit_template_142.hoc', cellName='motor_unit_142', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_143', conds={'cellType': 'MU', 'cellModel': 'Kim_143'}, 
	fileName='motor_unit_template_143.hoc', cellName='motor_unit_143', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_144', conds={'cellType': 'MU', 'cellModel': 'Kim_144'}, 
	fileName='motor_unit_template_144.hoc', cellName='motor_unit_144', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_145', conds={'cellType': 'MU', 'cellModel': 'Kim_145'}, 
	fileName='motor_unit_template_145.hoc', cellName='motor_unit_145', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_146', conds={'cellType': 'MU', 'cellModel': 'Kim_146'}, 
	fileName='motor_unit_template_146.hoc', cellName='motor_unit_146', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_147', conds={'cellType': 'MU', 'cellModel': 'Kim_147'}, 
	fileName='motor_unit_template_147.hoc', cellName='motor_unit_147', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_148', conds={'cellType': 'MU', 'cellModel': 'Kim_148'}, 
	fileName='motor_unit_template_148.hoc', cellName='motor_unit_148', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_149', conds={'cellType': 'MU', 'cellModel': 'Kim_149'}, 
	fileName='motor_unit_template_149.hoc', cellName='motor_unit_149', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_150', conds={'cellType': 'MU', 'cellModel': 'Kim_150'}, 
	fileName='motor_unit_template_150.hoc', cellName='motor_unit_150', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_151', conds={'cellType': 'MU', 'cellModel': 'Kim_151'}, 
	fileName='motor_unit_template_151.hoc', cellName='motor_unit_151', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_152', conds={'cellType': 'MU', 'cellModel': 'Kim_152'}, 
	fileName='motor_unit_template_152.hoc', cellName='motor_unit_152', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_153', conds={'cellType': 'MU', 'cellModel': 'Kim_153'}, 
	fileName='motor_unit_template_153.hoc', cellName='motor_unit_153', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_154', conds={'cellType': 'MU', 'cellModel': 'Kim_154'}, 
	fileName='motor_unit_template_154.hoc', cellName='motor_unit_154', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_155', conds={'cellType': 'MU', 'cellModel': 'Kim_155'}, 
	fileName='motor_unit_template_155.hoc', cellName='motor_unit_155', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_156', conds={'cellType': 'MU', 'cellModel': 'Kim_156'}, 
	fileName='motor_unit_template_156.hoc', cellName='motor_unit_156', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_157', conds={'cellType': 'MU', 'cellModel': 'Kim_157'}, 
	fileName='motor_unit_template_157.hoc', cellName='motor_unit_157', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_158', conds={'cellType': 'MU', 'cellModel': 'Kim_158'}, 
	fileName='motor_unit_template_158.hoc', cellName='motor_unit_158', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_159', conds={'cellType': 'MU', 'cellModel': 'Kim_159'}, 
	fileName='motor_unit_template_159.hoc', cellName='motor_unit_159', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_160', conds={'cellType': 'MU', 'cellModel': 'Kim_160'}, 
	fileName='motor_unit_template_160.hoc', cellName='motor_unit_160', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_161', conds={'cellType': 'MU', 'cellModel': 'Kim_161'}, 
	fileName='motor_unit_template_161.hoc', cellName='motor_unit_161', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_162', conds={'cellType': 'MU', 'cellModel': 'Kim_162'}, 
	fileName='motor_unit_template_162.hoc', cellName='motor_unit_162', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_163', conds={'cellType': 'MU', 'cellModel': 'Kim_163'}, 
	fileName='motor_unit_template_163.hoc', cellName='motor_unit_163', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_164', conds={'cellType': 'MU', 'cellModel': 'Kim_164'}, 
	fileName='motor_unit_template_164.hoc', cellName='motor_unit_164', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_165', conds={'cellType': 'MU', 'cellModel': 'Kim_165'}, 
	fileName='motor_unit_template_165.hoc', cellName='motor_unit_165', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_166', conds={'cellType': 'MU', 'cellModel': 'Kim_166'}, 
	fileName='motor_unit_template_166.hoc', cellName='motor_unit_166', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_167', conds={'cellType': 'MU', 'cellModel': 'Kim_167'}, 
	fileName='motor_unit_template_167.hoc', cellName='motor_unit_167', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_168', conds={'cellType': 'MU', 'cellModel': 'Kim_168'}, 
	fileName='motor_unit_template_168.hoc', cellName='motor_unit_168', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_169', conds={'cellType': 'MU', 'cellModel': 'Kim_169'}, 
	fileName='motor_unit_template_169.hoc', cellName='motor_unit_169', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_170', conds={'cellType': 'MU', 'cellModel': 'Kim_170'}, 
	fileName='motor_unit_template_170.hoc', cellName='motor_unit_170', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_171', conds={'cellType': 'MU', 'cellModel': 'Kim_171'}, 
	fileName='motor_unit_template_171.hoc', cellName='motor_unit_171', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_172', conds={'cellType': 'MU', 'cellModel': 'Kim_172'}, 
	fileName='motor_unit_template_172.hoc', cellName='motor_unit_172', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_173', conds={'cellType': 'MU', 'cellModel': 'Kim_173'}, 
	fileName='motor_unit_template_173.hoc', cellName='motor_unit_173', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_174', conds={'cellType': 'MU', 'cellModel': 'Kim_174'}, 
	fileName='motor_unit_template_174.hoc', cellName='motor_unit_174', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_175', conds={'cellType': 'MU', 'cellModel': 'Kim_175'}, 
	fileName='motor_unit_template_175.hoc', cellName='motor_unit_175', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_176', conds={'cellType': 'MU', 'cellModel': 'Kim_176'}, 
	fileName='motor_unit_template_176.hoc', cellName='motor_unit_176', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_177', conds={'cellType': 'MU', 'cellModel': 'Kim_177'}, 
	fileName='motor_unit_template_177.hoc', cellName='motor_unit_177', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_178', conds={'cellType': 'MU', 'cellModel': 'Kim_178'}, 
	fileName='motor_unit_template_178.hoc', cellName='motor_unit_178', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_179', conds={'cellType': 'MU', 'cellModel': 'Kim_179'}, 
	fileName='motor_unit_template_179.hoc', cellName='motor_unit_179', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_180', conds={'cellType': 'MU', 'cellModel': 'Kim_180'}, 
	fileName='motor_unit_template_180.hoc', cellName='motor_unit_180', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_181', conds={'cellType': 'MU', 'cellModel': 'Kim_181'}, 
	fileName='motor_unit_template_181.hoc', cellName='motor_unit_181', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_182', conds={'cellType': 'MU', 'cellModel': 'Kim_182'}, 
	fileName='motor_unit_template_182.hoc', cellName='motor_unit_182', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_183', conds={'cellType': 'MU', 'cellModel': 'Kim_183'}, 
	fileName='motor_unit_template_183.hoc', cellName='motor_unit_183', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_184', conds={'cellType': 'MU', 'cellModel': 'Kim_184'}, 
	fileName='motor_unit_template_184.hoc', cellName='motor_unit_184', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_185', conds={'cellType': 'MU', 'cellModel': 'Kim_185'}, 
	fileName='motor_unit_template_185.hoc', cellName='motor_unit_185', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_186', conds={'cellType': 'MU', 'cellModel': 'Kim_186'}, 
	fileName='motor_unit_template_186.hoc', cellName='motor_unit_186', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_187', conds={'cellType': 'MU', 'cellModel': 'Kim_187'}, 
	fileName='motor_unit_template_187.hoc', cellName='motor_unit_187', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_188', conds={'cellType': 'MU', 'cellModel': 'Kim_188'}, 
	fileName='motor_unit_template_188.hoc', cellName='motor_unit_188', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_189', conds={'cellType': 'MU', 'cellModel': 'Kim_189'}, 
	fileName='motor_unit_template_189.hoc', cellName='motor_unit_189', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_190', conds={'cellType': 'MU', 'cellModel': 'Kim_190'}, 
	fileName='motor_unit_template_190.hoc', cellName='motor_unit_190', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_191', conds={'cellType': 'MU', 'cellModel': 'Kim_191'}, 
	fileName='motor_unit_template_191.hoc', cellName='motor_unit_191', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_192', conds={'cellType': 'MU', 'cellModel': 'Kim_192'}, 
	fileName='motor_unit_template_192.hoc', cellName='motor_unit_192', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_193', conds={'cellType': 'MU', 'cellModel': 'Kim_193'}, 
	fileName='motor_unit_template_193.hoc', cellName='motor_unit_193', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_194', conds={'cellType': 'MU', 'cellModel': 'Kim_194'}, 
	fileName='motor_unit_template_194.hoc', cellName='motor_unit_194', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_195', conds={'cellType': 'MU', 'cellModel': 'Kim_195'}, 
	fileName='motor_unit_template_195.hoc', cellName='motor_unit_195', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_196', conds={'cellType': 'MU', 'cellModel': 'Kim_196'}, 
	fileName='motor_unit_template_196.hoc', cellName='motor_unit_196', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_197', conds={'cellType': 'MU', 'cellModel': 'Kim_197'}, 
	fileName='motor_unit_template_197.hoc', cellName='motor_unit_197', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_198', conds={'cellType': 'MU', 'cellModel': 'Kim_198'}, 
	fileName='motor_unit_template_198.hoc', cellName='motor_unit_198', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_199', conds={'cellType': 'MU', 'cellModel': 'Kim_199'}, 
	fileName='motor_unit_template_199.hoc', cellName='motor_unit_199', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_200', conds={'cellType': 'MU', 'cellModel': 'Kim_200'}, 
	fileName='motor_unit_template_200.hoc', cellName='motor_unit_200', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_201', conds={'cellType': 'MU', 'cellModel': 'Kim_201'}, 
	fileName='motor_unit_template_201.hoc', cellName='motor_unit_201', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_202', conds={'cellType': 'MU', 'cellModel': 'Kim_202'}, 
	fileName='motor_unit_template_202.hoc', cellName='motor_unit_202', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_203', conds={'cellType': 'MU', 'cellModel': 'Kim_203'}, 
	fileName='motor_unit_template_203.hoc', cellName='motor_unit_203', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_204', conds={'cellType': 'MU', 'cellModel': 'Kim_204'}, 
	fileName='motor_unit_template_204.hoc', cellName='motor_unit_204', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_205', conds={'cellType': 'MU', 'cellModel': 'Kim_205'}, 
	fileName='motor_unit_template_205.hoc', cellName='motor_unit_205', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_206', conds={'cellType': 'MU', 'cellModel': 'Kim_206'}, 
	fileName='motor_unit_template_206.hoc', cellName='motor_unit_206', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_207', conds={'cellType': 'MU', 'cellModel': 'Kim_207'}, 
	fileName='motor_unit_template_207.hoc', cellName='motor_unit_207', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_208', conds={'cellType': 'MU', 'cellModel': 'Kim_208'}, 
	fileName='motor_unit_template_208.hoc', cellName='motor_unit_208', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_209', conds={'cellType': 'MU', 'cellModel': 'Kim_209'}, 
	fileName='motor_unit_template_209.hoc', cellName='motor_unit_209', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_210', conds={'cellType': 'MU', 'cellModel': 'Kim_210'}, 
	fileName='motor_unit_template_210.hoc', cellName='motor_unit_210', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_211', conds={'cellType': 'MU', 'cellModel': 'Kim_211'}, 
	fileName='motor_unit_template_211.hoc', cellName='motor_unit_211', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_212', conds={'cellType': 'MU', 'cellModel': 'Kim_212'}, 
	fileName='motor_unit_template_212.hoc', cellName='motor_unit_212', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_213', conds={'cellType': 'MU', 'cellModel': 'Kim_213'}, 
	fileName='motor_unit_template_213.hoc', cellName='motor_unit_213', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_214', conds={'cellType': 'MU', 'cellModel': 'Kim_214'}, 
	fileName='motor_unit_template_214.hoc', cellName='motor_unit_214', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_215', conds={'cellType': 'MU', 'cellModel': 'Kim_215'}, 
	fileName='motor_unit_template_215.hoc', cellName='motor_unit_215', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_216', conds={'cellType': 'MU', 'cellModel': 'Kim_216'}, 
	fileName='motor_unit_template_216.hoc', cellName='motor_unit_216', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_217', conds={'cellType': 'MU', 'cellModel': 'Kim_217'}, 
	fileName='motor_unit_template_217.hoc', cellName='motor_unit_217', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_218', conds={'cellType': 'MU', 'cellModel': 'Kim_218'}, 
	fileName='motor_unit_template_218.hoc', cellName='motor_unit_218', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_219', conds={'cellType': 'MU', 'cellModel': 'Kim_219'}, 
	fileName='motor_unit_template_219.hoc', cellName='motor_unit_219', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_220', conds={'cellType': 'MU', 'cellModel': 'Kim_220'}, 
	fileName='motor_unit_template_220.hoc', cellName='motor_unit_220', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_221', conds={'cellType': 'MU', 'cellModel': 'Kim_221'}, 
	fileName='motor_unit_template_221.hoc', cellName='motor_unit_221', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_222', conds={'cellType': 'MU', 'cellModel': 'Kim_222'}, 
	fileName='motor_unit_template_222.hoc', cellName='motor_unit_222', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_223', conds={'cellType': 'MU', 'cellModel': 'Kim_223'}, 
	fileName='motor_unit_template_223.hoc', cellName='motor_unit_223', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_224', conds={'cellType': 'MU', 'cellModel': 'Kim_224'}, 
	fileName='motor_unit_template_224.hoc', cellName='motor_unit_224', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_225', conds={'cellType': 'MU', 'cellModel': 'Kim_225'}, 
	fileName='motor_unit_template_225.hoc', cellName='motor_unit_225', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_226', conds={'cellType': 'MU', 'cellModel': 'Kim_226'}, 
	fileName='motor_unit_template_226.hoc', cellName='motor_unit_226', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_227', conds={'cellType': 'MU', 'cellModel': 'Kim_227'}, 
	fileName='motor_unit_template_227.hoc', cellName='motor_unit_227', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_228', conds={'cellType': 'MU', 'cellModel': 'Kim_228'}, 
	fileName='motor_unit_template_228.hoc', cellName='motor_unit_228', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_229', conds={'cellType': 'MU', 'cellModel': 'Kim_229'}, 
	fileName='motor_unit_template_229.hoc', cellName='motor_unit_229', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_230', conds={'cellType': 'MU', 'cellModel': 'Kim_230'}, 
	fileName='motor_unit_template_230.hoc', cellName='motor_unit_230', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_231', conds={'cellType': 'MU', 'cellModel': 'Kim_231'}, 
	fileName='motor_unit_template_231.hoc', cellName='motor_unit_231', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_232', conds={'cellType': 'MU', 'cellModel': 'Kim_232'}, 
	fileName='motor_unit_template_232.hoc', cellName='motor_unit_232', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_233', conds={'cellType': 'MU', 'cellModel': 'Kim_233'}, 
	fileName='motor_unit_template_233.hoc', cellName='motor_unit_233', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_234', conds={'cellType': 'MU', 'cellModel': 'Kim_234'}, 
	fileName='motor_unit_template_234.hoc', cellName='motor_unit_234', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_235', conds={'cellType': 'MU', 'cellModel': 'Kim_235'}, 
	fileName='motor_unit_template_235.hoc', cellName='motor_unit_235', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_236', conds={'cellType': 'MU', 'cellModel': 'Kim_236'}, 
	fileName='motor_unit_template_236.hoc', cellName='motor_unit_236', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_237', conds={'cellType': 'MU', 'cellModel': 'Kim_237'}, 
	fileName='motor_unit_template_237.hoc', cellName='motor_unit_237', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_238', conds={'cellType': 'MU', 'cellModel': 'Kim_238'}, 
	fileName='motor_unit_template_238.hoc', cellName='motor_unit_238', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_239', conds={'cellType': 'MU', 'cellModel': 'Kim_239'}, 
	fileName='motor_unit_template_239.hoc', cellName='motor_unit_239', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_240', conds={'cellType': 'MU', 'cellModel': 'Kim_240'}, 
	fileName='motor_unit_template_240.hoc', cellName='motor_unit_240', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_241', conds={'cellType': 'MU', 'cellModel': 'Kim_241'}, 
	fileName='motor_unit_template_241.hoc', cellName='motor_unit_241', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_242', conds={'cellType': 'MU', 'cellModel': 'Kim_242'}, 
	fileName='motor_unit_template_242.hoc', cellName='motor_unit_242', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_243', conds={'cellType': 'MU', 'cellModel': 'Kim_243'}, 
	fileName='motor_unit_template_243.hoc', cellName='motor_unit_243', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_244', conds={'cellType': 'MU', 'cellModel': 'Kim_244'}, 
	fileName='motor_unit_template_244.hoc', cellName='motor_unit_244', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_245', conds={'cellType': 'MU', 'cellModel': 'Kim_245'}, 
	fileName='motor_unit_template_245.hoc', cellName='motor_unit_245', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_246', conds={'cellType': 'MU', 'cellModel': 'Kim_246'}, 
	fileName='motor_unit_template_246.hoc', cellName='motor_unit_246', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_247', conds={'cellType': 'MU', 'cellModel': 'Kim_247'}, 
	fileName='motor_unit_template_247.hoc', cellName='motor_unit_247', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_248', conds={'cellType': 'MU', 'cellModel': 'Kim_248'}, 
	fileName='motor_unit_template_248.hoc', cellName='motor_unit_248', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_249', conds={'cellType': 'MU', 'cellModel': 'Kim_249'}, 
	fileName='motor_unit_template_249.hoc', cellName='motor_unit_249', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_250', conds={'cellType': 'MU', 'cellModel': 'Kim_250'}, 
	fileName='motor_unit_template_250.hoc', cellName='motor_unit_250', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_251', conds={'cellType': 'MU', 'cellModel': 'Kim_251'}, 
	fileName='motor_unit_template_251.hoc', cellName='motor_unit_251', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_252', conds={'cellType': 'MU', 'cellModel': 'Kim_252'}, 
	fileName='motor_unit_template_252.hoc', cellName='motor_unit_252', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_253', conds={'cellType': 'MU', 'cellModel': 'Kim_253'}, 
	fileName='motor_unit_template_253.hoc', cellName='motor_unit_253', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_254', conds={'cellType': 'MU', 'cellModel': 'Kim_254'}, 
	fileName='motor_unit_template_254.hoc', cellName='motor_unit_254', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_255', conds={'cellType': 'MU', 'cellModel': 'Kim_255'}, 
	fileName='motor_unit_template_255.hoc', cellName='motor_unit_255', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_256', conds={'cellType': 'MU', 'cellModel': 'Kim_256'}, 
	fileName='motor_unit_template_256.hoc', cellName='motor_unit_256', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_257', conds={'cellType': 'MU', 'cellModel': 'Kim_257'}, 
	fileName='motor_unit_template_257.hoc', cellName='motor_unit_257', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_258', conds={'cellType': 'MU', 'cellModel': 'Kim_258'}, 
	fileName='motor_unit_template_258.hoc', cellName='motor_unit_258', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_259', conds={'cellType': 'MU', 'cellModel': 'Kim_259'}, 
	fileName='motor_unit_template_259.hoc', cellName='motor_unit_259', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_260', conds={'cellType': 'MU', 'cellModel': 'Kim_260'}, 
	fileName='motor_unit_template_260.hoc', cellName='motor_unit_260', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_261', conds={'cellType': 'MU', 'cellModel': 'Kim_261'}, 
	fileName='motor_unit_template_261.hoc', cellName='motor_unit_261', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_262', conds={'cellType': 'MU', 'cellModel': 'Kim_262'}, 
	fileName='motor_unit_template_262.hoc', cellName='motor_unit_262', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_263', conds={'cellType': 'MU', 'cellModel': 'Kim_263'}, 
	fileName='motor_unit_template_263.hoc', cellName='motor_unit_263', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_264', conds={'cellType': 'MU', 'cellModel': 'Kim_264'}, 
	fileName='motor_unit_template_264.hoc', cellName='motor_unit_264', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_265', conds={'cellType': 'MU', 'cellModel': 'Kim_265'}, 
	fileName='motor_unit_template_265.hoc', cellName='motor_unit_265', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_266', conds={'cellType': 'MU', 'cellModel': 'Kim_266'}, 
	fileName='motor_unit_template_266.hoc', cellName='motor_unit_266', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_267', conds={'cellType': 'MU', 'cellModel': 'Kim_267'}, 
	fileName='motor_unit_template_267.hoc', cellName='motor_unit_267', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_268', conds={'cellType': 'MU', 'cellModel': 'Kim_268'}, 
	fileName='motor_unit_template_268.hoc', cellName='motor_unit_268', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_269', conds={'cellType': 'MU', 'cellModel': 'Kim_269'}, 
	fileName='motor_unit_template_269.hoc', cellName='motor_unit_269', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_270', conds={'cellType': 'MU', 'cellModel': 'Kim_270'}, 
	fileName='motor_unit_template_270.hoc', cellName='motor_unit_270', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_271', conds={'cellType': 'MU', 'cellModel': 'Kim_271'}, 
	fileName='motor_unit_template_271.hoc', cellName='motor_unit_271', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_272', conds={'cellType': 'MU', 'cellModel': 'Kim_272'}, 
	fileName='motor_unit_template_272.hoc', cellName='motor_unit_272', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_273', conds={'cellType': 'MU', 'cellModel': 'Kim_273'}, 
	fileName='motor_unit_template_273.hoc', cellName='motor_unit_273', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_274', conds={'cellType': 'MU', 'cellModel': 'Kim_274'}, 
	fileName='motor_unit_template_274.hoc', cellName='motor_unit_274', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_275', conds={'cellType': 'MU', 'cellModel': 'Kim_275'}, 
	fileName='motor_unit_template_275.hoc', cellName='motor_unit_275', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_276', conds={'cellType': 'MU', 'cellModel': 'Kim_276'}, 
	fileName='motor_unit_template_276.hoc', cellName='motor_unit_276', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_277', conds={'cellType': 'MU', 'cellModel': 'Kim_277'}, 
	fileName='motor_unit_template_277.hoc', cellName='motor_unit_277', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_278', conds={'cellType': 'MU', 'cellModel': 'Kim_278'}, 
	fileName='motor_unit_template_278.hoc', cellName='motor_unit_278', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_279', conds={'cellType': 'MU', 'cellModel': 'Kim_279'}, 
	fileName='motor_unit_template_279.hoc', cellName='motor_unit_279', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_280', conds={'cellType': 'MU', 'cellModel': 'Kim_280'}, 
	fileName='motor_unit_template_280.hoc', cellName='motor_unit_280', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_281', conds={'cellType': 'MU', 'cellModel': 'Kim_281'}, 
	fileName='motor_unit_template_281.hoc', cellName='motor_unit_281', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_282', conds={'cellType': 'MU', 'cellModel': 'Kim_282'}, 
	fileName='motor_unit_template_282.hoc', cellName='motor_unit_282', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_283', conds={'cellType': 'MU', 'cellModel': 'Kim_283'}, 
	fileName='motor_unit_template_283.hoc', cellName='motor_unit_283', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_284', conds={'cellType': 'MU', 'cellModel': 'Kim_284'}, 
	fileName='motor_unit_template_284.hoc', cellName='motor_unit_284', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_285', conds={'cellType': 'MU', 'cellModel': 'Kim_285'}, 
	fileName='motor_unit_template_285.hoc', cellName='motor_unit_285', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_286', conds={'cellType': 'MU', 'cellModel': 'Kim_286'}, 
	fileName='motor_unit_template_286.hoc', cellName='motor_unit_286', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_287', conds={'cellType': 'MU', 'cellModel': 'Kim_287'}, 
	fileName='motor_unit_template_287.hoc', cellName='motor_unit_287', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_288', conds={'cellType': 'MU', 'cellModel': 'Kim_288'}, 
	fileName='motor_unit_template_288.hoc', cellName='motor_unit_288', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_289', conds={'cellType': 'MU', 'cellModel': 'Kim_289'}, 
	fileName='motor_unit_template_289.hoc', cellName='motor_unit_289', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_290', conds={'cellType': 'MU', 'cellModel': 'Kim_290'}, 
	fileName='motor_unit_template_290.hoc', cellName='motor_unit_290', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_291', conds={'cellType': 'MU', 'cellModel': 'Kim_291'}, 
	fileName='motor_unit_template_291.hoc', cellName='motor_unit_291', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_292', conds={'cellType': 'MU', 'cellModel': 'Kim_292'}, 
	fileName='motor_unit_template_292.hoc', cellName='motor_unit_292', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_293', conds={'cellType': 'MU', 'cellModel': 'Kim_293'}, 
	fileName='motor_unit_template_293.hoc', cellName='motor_unit_293', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_294', conds={'cellType': 'MU', 'cellModel': 'Kim_294'}, 
	fileName='motor_unit_template_294.hoc', cellName='motor_unit_294', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_295', conds={'cellType': 'MU', 'cellModel': 'Kim_295'}, 
	fileName='motor_unit_template_295.hoc', cellName='motor_unit_295', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_296', conds={'cellType': 'MU', 'cellModel': 'Kim_296'}, 
	fileName='motor_unit_template_296.hoc', cellName='motor_unit_296', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_297', conds={'cellType': 'MU', 'cellModel': 'Kim_297'}, 
	fileName='motor_unit_template_297.hoc', cellName='motor_unit_297', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_298', conds={'cellType': 'MU', 'cellModel': 'Kim_298'}, 
	fileName='motor_unit_template_298.hoc', cellName='motor_unit_298', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_299', conds={'cellType': 'MU', 'cellModel': 'Kim_299'}, 
	fileName='motor_unit_template_299.hoc', cellName='motor_unit_299', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_300', conds={'cellType': 'MU', 'cellModel': 'Kim_300'}, 
	fileName='motor_unit_template_300.hoc', cellName='motor_unit_300', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_301', conds={'cellType': 'MU', 'cellModel': 'Kim_301'}, 
	fileName='motor_unit_template_301.hoc', cellName='motor_unit_301', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_302', conds={'cellType': 'MU', 'cellModel': 'Kim_302'}, 
	fileName='motor_unit_template_302.hoc', cellName='motor_unit_302', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_303', conds={'cellType': 'MU', 'cellModel': 'Kim_303'}, 
	fileName='motor_unit_template_303.hoc', cellName='motor_unit_303', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_304', conds={'cellType': 'MU', 'cellModel': 'Kim_304'}, 
	fileName='motor_unit_template_304.hoc', cellName='motor_unit_304', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_305', conds={'cellType': 'MU', 'cellModel': 'Kim_305'}, 
	fileName='motor_unit_template_305.hoc', cellName='motor_unit_305', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_306', conds={'cellType': 'MU', 'cellModel': 'Kim_306'}, 
	fileName='motor_unit_template_306.hoc', cellName='motor_unit_306', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_307', conds={'cellType': 'MU', 'cellModel': 'Kim_307'}, 
	fileName='motor_unit_template_307.hoc', cellName='motor_unit_307', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_308', conds={'cellType': 'MU', 'cellModel': 'Kim_308'}, 
	fileName='motor_unit_template_308.hoc', cellName='motor_unit_308', importSynMechs=True, somaAtOrigin=False)	
cellRule = netParams.importCellParams(label='motor_unit_309', conds={'cellType': 'MU', 'cellModel': 'Kim_309'}, 
	fileName='motor_unit_template_309.hoc', cellName='motor_unit_309', importSynMechs=True, somaAtOrigin=False)
cellRule = netParams.importCellParams(label='motor_unit_310', conds={'cellType': 'MU', 'cellModel': 'Kim_310'}, 
	fileName='motor_unit_template_310.hoc', cellName='motor_unit_310', importSynMechs=True, somaAtOrigin=False)
	
	
## Synaptic mechanism parameters
# This is the type of synapse between connected cells.
#  Use netParams.synMechParams['name_syn'] = to define.
# In this study, each MU is an independent signal.

## Stimulation parameters
# Apply stimulation uniformly to all cells in neuronal network. Each cell must have a unique stimulation
#  or else it will not work properly.
netParams.stimSourceParams['i_clamp'] = {'type': 'RampIClampNoise'}
netParams.stimTargetParams['bg_1'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_1'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_2'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_2'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_3'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_3'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_4'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_4'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_5'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_5'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_6'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_6'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_7'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_7'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_8'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_8'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_9'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_9'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_10'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_10'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_11'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_11'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_12'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_12'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_13'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_13'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_14'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_14'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_15'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_15'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_16'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_16'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_17'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_17'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_18'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_18'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_19'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_19'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_20'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_20'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_21'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_21'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_22'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_22'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_23'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_23'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_24'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_24'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_25'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_25'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_26'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_26'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_27'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_27'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_28'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_28'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_29'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_29'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_30'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_30'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_31'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_31'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_32'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_32'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_33'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_33'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_34'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_34'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_35'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_35'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_36'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_36'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_37'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_37'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_38'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_38'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_39'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_39'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_40'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_40'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_41'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_41'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_42'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_42'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_43'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_43'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_44'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_44'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_45'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_45'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_46'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_46'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_47'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_47'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_48'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_48'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_49'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_49'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_50'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_50'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_51'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_51'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_52'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_52'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_53'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_53'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_54'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_54'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_55'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_55'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_56'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_56'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_57'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_57'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_58'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_58'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_59'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_59'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_60'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_60'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_61'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_61'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_62'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_62'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_63'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_63'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_64'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_64'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_65'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_65'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_66'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_66'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_67'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_67'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_68'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_68'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_69'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_69'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_70'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_70'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_71'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_71'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_72'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_72'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_73'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_73'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_74'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_74'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_75'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_75'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_76'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_76'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_77'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_77'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_78'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_78'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_79'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_79'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_80'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_80'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_81'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_81'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_82'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_82'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_83'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_83'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_84'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_84'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_85'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_85'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_86'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_86'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_87'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_87'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_88'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_88'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_89'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_89'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_90'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_90'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_91'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_91'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_92'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_92'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_93'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_93'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_94'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_94'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_95'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_95'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_96'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_96'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_97'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_97'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_98'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_98'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_99'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_99'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_100'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_100'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_101'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_101'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_102'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_102'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_103'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_103'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_104'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_104'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_105'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_105'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_106'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_106'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_107'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_107'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_108'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_108'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_109'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_109'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_110'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_110'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_111'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_111'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_112'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_112'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_113'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_113'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_114'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_114'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_115'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_115'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_116'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_116'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_117'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_117'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_118'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_118'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_119'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_119'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_120'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_120'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_121'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_121'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_122'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_122'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_123'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_123'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_124'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_124'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_125'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_125'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_126'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_126'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_127'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_127'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_128'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_128'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_129'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_129'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_130'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_130'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_131'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_131'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_132'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_132'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_133'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_133'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_134'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_134'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_135'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_135'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_136'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_136'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_137'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_137'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_138'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_138'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_139'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_139'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_140'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_140'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_141'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_141'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_142'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_142'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_143'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_143'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_144'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_144'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_145'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_145'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_146'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_146'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_147'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_147'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_148'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_148'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_149'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_149'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_150'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_150'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_151'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_151'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_152'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_152'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_153'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_153'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_154'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_154'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_155'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_155'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_156'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_156'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_157'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_157'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_158'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_158'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_159'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_159'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_160'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_160'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_161'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_161'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_162'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_162'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_163'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_163'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_164'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_164'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_165'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_165'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_166'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_166'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_167'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_167'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_168'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_168'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_169'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_169'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_170'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_170'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_171'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_171'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_172'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_172'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_173'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_173'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_174'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_174'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_175'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_175'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_176'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_176'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_177'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_177'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_178'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_178'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_179'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_179'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_180'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_180'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_181'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_181'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_182'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_182'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_183'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_183'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_184'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_184'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_185'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_185'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_186'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_186'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_187'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_187'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_188'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_188'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_189'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_189'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_190'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_190'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_191'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_191'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_192'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_192'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_193'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_193'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_194'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_194'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_195'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_195'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_196'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_196'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_197'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_197'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_198'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_198'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_199'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_199'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_200'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_200'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_201'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_201'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_202'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_202'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_203'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_203'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_204'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_204'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_205'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_205'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_206'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_206'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_207'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_207'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_208'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_208'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_209'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_209'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_210'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_210'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_211'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_211'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_212'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_212'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_213'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_213'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_214'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_214'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_215'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_215'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_216'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_216'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_217'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_217'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_218'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_218'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_219'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_219'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_220'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_220'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_221'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_221'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_222'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_222'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_223'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_223'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_224'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_224'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_225'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_225'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_226'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_226'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_227'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_227'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_228'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_228'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_229'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_229'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_230'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_230'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_231'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_231'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_232'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_232'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_233'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_233'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_234'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_234'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_235'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_235'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_236'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_236'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_237'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_237'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_238'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_238'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_239'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_239'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_240'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_240'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_241'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_241'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_242'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_242'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_243'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_243'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_244'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_244'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_245'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_245'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_246'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_246'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_247'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_247'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_248'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_248'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_249'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_249'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_250'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_250'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_251'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_251'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_252'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_252'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_253'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_253'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_254'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_254'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_255'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_255'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_256'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_256'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_257'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_257'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_258'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_258'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_259'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_259'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_260'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_260'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_261'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_261'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_262'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_262'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_263'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_263'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_264'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_264'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_265'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_265'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_266'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_266'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_267'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_267'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_268'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_268'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_269'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_269'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_270'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_270'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_271'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_271'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_272'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_272'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_273'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_273'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_274'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_274'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_275'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_275'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_276'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_276'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_277'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_277'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_278'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_278'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_279'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_279'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_280'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_280'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_281'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_281'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_282'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_282'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_283'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_283'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_284'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_284'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_285'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_285'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_286'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_286'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_287'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_287'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_288'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_288'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_289'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_289'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_290'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_290'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_291'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_291'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_292'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_292'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_293'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_293'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_294'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_294'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_295'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_295'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_296'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_296'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_297'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_297'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_298'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_298'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_299'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_299'}, 
									'sec': 'soma', 'loc': 0.5}																																																																																																																																																																		
netParams.stimTargetParams['bg_300'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_300'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_301'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_301'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_302'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_302'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_303'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_303'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_304'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_304'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_305'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_305'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_306'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_306'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_307'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_307'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_308'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_308'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_309'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_309'}, 
									'sec': 'soma', 'loc': 0.5}
netParams.stimTargetParams['bg_310'] = {'source': 'i_clamp', 'conds': {'cellType': 'MU', 'cellModel': 'Kim_310'}, 
									'sec': 'soma', 'loc': 0.5}									

## Connectivity parameters
# Here is the space to define which cells/populations are connected to one another, and define
#  the parameters (weight, delay, randomness) of the connections. In this model, the motor neurons
#  are not connected together because their effects on one another occur during force transmission
#  and are not an electrochemical communication.

## Simulation options
# Define the simulation parameters
simConfig = specs.SimConfig()		#object of class SimConfig to store simulation configuration
simConfig.hParams = {'v_init': -70.0, 'celsius': 36}
simConfig.duration = 3000		# duration of the simulation (ms)
simConfig.dt = 0.025			# internal integration timestep to use (0.025 NEURON default)
simConfig.verbose = 0			# show detailed messages
simConfig.recordCells = {'all'}
simConfig.recordTraces = {'mgi_musc':{'sec':'muscle_unit', 'loc':0.5, 'var':'mgi'}, 'cli_musc':{'sec':'muscle_unit', 'loc':0.5, 'var':'cli'}}
# Additional traces to add that might be useful for data analyses:
#  {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}} and {'V_musc':{'sec':'muscle_unit', 'loc':0.5, 'var':'v'}}
simConfig.recordStep = 0.025		# step size in ms to save data
simConfig.filename = 'model output'		# set file output name
simConfig.savePickle = True 		# Save params, network and sim output to pickle file

simConfig.analysis['plotRaster'] = {'orderInverse': True, 'saveFig': 'NMS_raster.png', 'saveData': True}		# plot a raster
simConfig.analysis['plotTraces'] = {'include': {'all'}, 'saveData': True}		# save data from traces to pkl file

# CREATE SIMULATE ANALYZE  NETWORK ---------------------------------------------
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)

# END SCRIPT ===================================================================
