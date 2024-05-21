from b_process_input_file import *

def create_sbt(site):
    '''Create SixBitTask Automation Node Instances'''
    units_phases = process_units_phases()
    units_phases["UnitPhase"] = units_phases["Unit"] + units_phases["Phase"]
    sbt_name_list = units_phases["UnitPhase"].tolist()
    sbt_list = ''
    for name in sbt_name_list:
        sbt_list = sbt_list + f'"SixBitTask","{name}","{name}","","{site}"' +'\n'
    return sbt_list