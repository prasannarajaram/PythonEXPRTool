from b_process_input_file import *
import re
import pdb


def create_automation_node_instance_rep(site):
    '''Create Automation Node Instance Report'''
    units_phases = process_units_phases()
    units_phases["PhaseRep"] = units_phases["Phase"] + 'Report'
    units_phases["UnitPhaseRep"] = units_phases["Unit"] + units_phases["PhaseRep"]
    anir = ''
    for UnitNumber, PhaseRep, UnitPhaseRep in zip(units_phases["Unit"].tolist(), units_phases["PhaseRep"].tolist(), units_phases["UnitPhaseRep"].tolist()):
        unit_num_pattern = r'\d+'
        # pdb.set_trace()
        unit_no_prefix = int(re.findall(unit_num_pattern, UnitNumber)[0])
        report_typicals = ["AddToRecLineReport", "DigestionReport", "DoseFTReport", "DoseReport",
                           "DrainDrumReport", "DrainFromMMReport", "DrainReport", "FlushReport",
                           "GasBaDoseFTReport", "GasBaDoseReport", "IFUReceiveReport", "MFUReceiveReport", "MixReport",
                           "PiggingReport", "PremixerDoseReport", "ReceiveByDSReport", "ReceiveByFTReport",
                           "ReceiveByWTReport", "ReceiveFromDrumReport", "ReceiveFromMMReport", "ReceiveParallelReport",
                           "RecycleReport", "RecycleSampleReport", "StopDoseFTReport", "StopDoseWTReport",
                           "TLUReceiveReport", "TransferToPackReport", "TrDrumReport", "WaitForAnalysisReport"]
        if PhaseRep in report_typicals:
            if "AddToRecLineReport" in PhaseRep: # Todo: Not configured in {site}, check Lote / ZJG / TLX
                anir = anir + f'**Error** AddToRecLineReport Report not configured' + '\n'
            if "DigestionReport" in PhaseRep:
                anir = anir + f'"{UnitNumber}DigestionReport","DigestionTime","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}DigestionTime","CyclicContinuous","Ti1s","None",""' + '\n'
            if "DoseFTReport" in PhaseRep:
                instrument_number = (unit_no_prefix * 10) + 8
                anir = anir + f'"{UnitNumber}DoseFTReport","TankNetWeightDosed","0","","{site}","NodeId","ns=1;s=t|HFT_{instrument_number}_1TOT","CyclicContinuous","Ti1s","None",""' + '\n'
            if "DoseReport" in PhaseRep: # Todo: Not configured in {site}, check Lote / ZJG / TLX
                anir = anir + f'**Error** DoseReport not configured' + '\n'
            if "DrainDrumReport" in PhaseRep: # Todo: Not configured in {site}, check Lote / ZJG / TLX
                anir = anir + f'**Error** DrainDrumReport not configured' + '\n'
            if "DrainFromMMReport" in PhaseRep:
                anir = anir + f'"{UnitNumber}DrainFromMMReport","Drain-From-MM-Drain-Timer","0","","{site}","NodeId","ns=1;s=t|AlwaysZero","CyclicContinuous","Ti1s","None",""' + '\n'
                anir = anir + f'"{UnitNumber}DrainFromMMReport","Drain-From-MM-Pause-Timer","0","","{site}","NodeId","ns=1;s=t|AlwaysZero","CyclicContinuous","Ti1s","None",""' + '\n'
                anir = anir + f'"{UnitNumber}DrainFromMMReport","Drain-Weight-SP","0","","{site}","NodeId","ns=1;s=t|WT_{unit_no_prefix}3NET","CyclicContinuous","Ti1s","None",""' + '\n'
                anir = anir + f'"{UnitNumber}DrainFromMMReport","Number-Of-Drain-Cycles","0","","{site}","NodeId","ns=1;s=t|AlwaysZero","CyclicContinuous","Ti1s","None",""' + '\n'
            if "DrainReport" in PhaseRep:
                anir = anir + f'"{UnitNumber}DrainReport","QuantityDrained","0","","{site}","NodeId","ns=1;s=t|WT_{unit_no_prefix}3NET","CyclicContinuous","Ti1s","None",""' + '\n'
            if "FlushReport" in PhaseRep: # Todo: Not configured in {site}, check Lote / ZJG / TLX
                anir = anir + f'**Error** FlushReport not configured' + '\n'
            if "GasBaDoseFTReport" in PhaseRep: # Todo: Not configured in {site}, check Lote / ZJG / TLX
                anir = anir + f'**Error** GasBaDoseFTReport not configured' + '\n'
            if "GasBaDoseReport" in PhaseRep: # Todo: Not configured in {site}, check Lote / ZJG / TLX
                anir = anir + f'**Error** GasBaDoseReport not configured' + '\n'
            if "IFUReceiveReport" in PhaseRep: # Todo: Not configured in {site}, check Lote / ZJG / TLX
                anir = anir + f'**Error** IFUReceiveReport not configured' + '\n'
            if "MFUReceiveReport" in PhaseRep:
                anir = anir + f'"{UnitNumber}MFUReceiveReport","NumberOfPackagedContainers","0","","{site}","NodeId","ns=1;s=t|AlwaysZero","CyclicContinuous","Ti1s","None",""' + '\n'
                anir = anir + f'"{UnitNumber}MFUReceiveReport","NumberOfPackagedPallets","0","","{site}","NodeId","ns=1;s=t|AlwaysZero","CyclicContinuous","Ti1s","None",""' + '\n'
                anir = anir + f'"{UnitNumber}MFUReceiveReport","PackagedQuantity","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}PackagedQuantity","CyclicContinuous","Ti1s","None","" ' + '\n'
            if "MixReport" in PhaseRep: ## remove this entry
                anir = anir + f'**Error** MixReport not configured' + '\n'
            if "PiggingReport" in PhaseRep: # Todo: Not configured in {site}, check Lote / ZJG / TLX
                anir = anir + f'**Error** PiggingReport not configured' + '\n'
            if "PremixerDoseReport" in PhaseRep:
                instrument_number = (unit_no_prefix * 10) + 3
                anir = anir + f'"{UnitNumber}PremixerDoseReport","TransferedQuantity","0","","{site}","NodeId","ns=1;s=t|WT_{instrument_number}NET","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveByDSReport" in PhaseRep: # Todo: Not configured in {site}, check Lote / ZJG / TLX
                anir = anir + f'**Error** ReceiveByDSReport not configured' + '\n'
            if "ReceiveByFTReport" in PhaseRep:
                instrument_number = (unit_no_prefix * 10) + 3
                anir = anir + f'"{UnitNumber}ReceiveByFTReport","RmDosedQuantity","0","","{site}","NodeId","ns=1;s=t|WT_{instrument_number}NET","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveByWTReport" in PhaseRep:
                instrument_number = (unit_no_prefix * 10) + 3
                anir = anir + f'"{UnitNumber}ReceiveByWTReport","RmDosedQuantity","0","","{site}","NodeId","ns=1;s=t|WT_{instrument_number}NET","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveFromDrumReport" in PhaseRep:
                instrument_number = (unit_no_prefix * 10) + 3
                anir = anir + f'"{UnitNumber}ReceiveFromDrumReport","RmDosedQuantity","0","","{site}","NodeId","ns=1;s=t|WT_{instrument_number}NET","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveFromMMReport" in PhaseRep:
                instrument_number = (unit_no_prefix * 10) + 3
                anir = anir + f'"{UnitNumber}ReceiveFromMMReport","RmDosedQuantity","0","","{site}","NodeId","ns=1;s=t|WT_{instrument_number}NET","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveParallelReport" in PhaseRep:
                anir = anir + f'**Error** ReceiveParallelReport not configured' + '\n'
            if "RecycleReport" in PhaseRep:
                anir = anir + f'"{UnitNumber}RecycleReport","RecycledTime","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}RecycleTimeCnt","CyclicContinuous","Ti1s","None",""' + '\n'
            if "RecycleSampleReport" in PhaseRep:
                anir = anir + f'"{UnitNumber}RecycleSampleReport","RecycledSmpTime","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}RecycleSmpTimeCnt","CyclicContinuous","Ti1s","None",""' + '\n'
            if "StopDoseFTReport" in PhaseRep: ## remove this entry
                anir = anir + f'**Error** StopDoseFTReport not configured' + '\n'
            if "StopDoseWTReport" in PhaseRep: ## remove this entry
                anir = anir + f'**Error** StopDoseWTReport not configured' + '\n'
            if "TLUReceiveReport" in PhaseRep:
                anir = anir + f'"{UnitNumber}TLUReceiveReport","PackagedQuantity","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}AmtLoaded","CyclicContinuous","Ti1s","None",""' + '\n'
                anir = anir + f'"{UnitNumber}TLUReceiveReport","TruckCabin1Quantity","0","","{site}","NodeId","ns=1;s=t|AlwaysZeroReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anir = anir + f'"{UnitNumber}TLUReceiveReport","TruckCabin2Quantity","0","","{site}","NodeId","ns=1;s=t|AlwaysZeroReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anir = anir + f'"{UnitNumber}TLUReceiveReport","TruckCabin3Quantity","0","","{site}","NodeId","ns=1;s=t|AlwaysZeroReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anir = anir + f'"{UnitNumber}TLUReceiveReport","TruckCabin4Quantity","0","","{site}","NodeId","ns=1;s=t|AlwaysZeroReal","CyclicContinuous","Ti1s","None",""' + '\n'
            if "TransferToPackReport" in PhaseRep:
                anir = anir + f'**Error** TransferToPackReport not configured' + '\n'
            if "TrDrumReport" in PhaseRep:
                anir = anir + f'"{UnitNumber}TrDrumReport","WaitForDedrummingTime","0","","JUNDIAI","NodeId","ns=1;s=t|{UnitNumber}WaitForDedrumCnt","CyclicContinuous","Ti1s","None",""' + '\n'
            if "WaitForAnalysisReport" in PhaseRep:
                anir = anir + f'"{UnitNumber}WaitForAnalysisReport","AnalysisTime","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}AnalysisTimeCnt","CyclicContinuous","Ti1s","None",""' + '\n'
        else:
            anir = anir + f'**Error** No matching phase name for {PhaseRep}. {UnitPhaseRep} automation node instance not created \n'
    return anir