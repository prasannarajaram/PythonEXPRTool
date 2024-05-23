from b_process_input_file import *

def create_sbt(site):
    '''Create SixBitTask Automation Node Instances'''
    units_phases = process_units_phases()
    units_phases["UnitPhase"] = units_phases["Unit"] + units_phases["Phase"]
    sbt_name_list = units_phases["UnitPhase"].tolist()
    sbt_list = ''
    for name in sbt_name_list:
        sbt_list = sbt_list + f'"SixBitTask","{name}","{name}","","{site}"' +'\n'
        sbt_list = sbt_list + f'"{name}","Abort","False","","{site}","NodeId","ns=1;s=t|{name}Abort","CyclicContinuous","Ti1s","None",""' + '\n'
        sbt_list = sbt_list + f'"{name}","Compl","False","","{site}","NodeId","ns=1;s=t|{name}Compl","CyclicContinuous","Ti1s","None",""' + '\n'
        sbt_list = sbt_list + f'"{name}","Pause","False","","{site}","NodeId","ns=1;s=t|{name}Pause","CyclicContinuous","Ti1s","None",""' + '\n'
        sbt_list = sbt_list + f'"{name}","Progr","False","","{site}","NodeId","ns=1;s=t|{name}Progr","CyclicContinuous","Ti1s","None",""' + '\n'
        sbt_list = sbt_list + f'"{name}","Start","False","","{site}","NodeId","ns=1;s=t|{name}Start","CyclicContinuous","Ti1s","None",""' + '\n'
    return sbt_list



