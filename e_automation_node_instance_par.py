from b_process_input_file import *
import re

def create_automation_node_instance_par(site):
    '''Create Automation Node Instance Parameter'''
    units_phases = process_units_phases()
    units_phases["PhasePar"] = units_phases["Phase"] + 'Parameters'
    units_phases["UnitPhasePar"] = units_phases["Unit"] + units_phases["PhasePar"]
    anip = ''
    for UnitNumber, PhasePar, UnitPhasePar in zip(units_phases["Unit"].tolist(), units_phases["PhasePar"].tolist(), units_phases["UnitPhasePar"].tolist()):
        unit_num_pattern = r'\d+'
        unit_no_prefix = int(re.findall(unit_num_pattern, UnitNumber)[0])
        parameter_typicals = ["AddToRecLineParameters", "DigestionParameters", "DrainParameters", "MixParameters", "ReceiveByFTParameters",
                            "ReceiveByWTParameters", "ReceiveFromDrumParameters", "RecycleParameters", "RecycleSampleParameters",
                            "TransferToPackParameters", "WaitForAnalysisParameters", "DrainDrumParameters",
                            "DoseFTParameters", "DoseParameters", "FlushParameters", "GasBaDoseFTParameters",
                            "GasBaDoseParameters", "IFUReceiveParameters", "MFUReceiveParameters",
                            "MMMixingParameters", "PiggingParameters", "PremixerDoseParameters", "ReceiveByDSParameters",
                            "ReceiveFromMMParameters", "ReceiveFromPremixerParameters", "ReceiveParallelParameters" ,
                            "StartDoseFTParameters", "StartDoseWTParameters", "StopDoseFTParameters", "StopDoseWTParameters",
                            "TLUReceiveParameters", "TrDrumParameters"]
        if PhasePar in parameter_typicals:
            if "DrainParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}DrainParameters","DrainSp","0","","{site}","NodeId","ns=1;s=t|WT_{UnitNumber}3SP","CyclicContinuous","Ti1s","None",""' + '\n'
            if "MixParameters" in PhasePar:
                anip = anip + f'**Error** Mix Parameters not configured' + '\n'
            if "ReceiveByFTParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}ReceiveByFTParameters","Queue","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}HFTQueue","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveByFTParameters","RmName","","","{site}","NodeId","ns=1;s=t|{UnitNumber}RmName","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveByFTParameters","SetPoint","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}HFTSP","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveByFTParameters","StorageTank","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}StorageTank","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveByWTParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}ReceiveByWTParameters","Queue","0","","{site}","NodeId","ns=1;s=t|WT_{UnitNumber}3QUEUE","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveByWTParameters","RmName","","","{site}","NodeId","ns=1;s=t|{UnitNumber}RmName","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveByWTParameters","SetPoint","0","","{site}","NodeId","ns=1;s=t|WT_{UnitNumber}3SP","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveByWTParameters","StorageTank","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}StorageTank","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveFromDrumParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}ReceiveFromDrumParameters","PumpFlowRate","0","","{site}","NodeId","ns=1;s=t|ScratchFloat","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveFromDrumParameters","Queue","0","","{site}","NodeId","ns=1;s=t|WT_{UnitNumber}3QUEUE","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveFromDrumParameters","RmName","","","{site}","NodeId","ns=1;s=t|{UnitNumber}RmName","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveFromDrumParameters","SetPoint","0","","{site}","NodeId","ns=1;s=t|WT_{UnitNumber}3SP","CyclicContinuous","Ti1s","None",""' + '\n'
            if "RecycleParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}RecycleParameters","AgitatorRunningForCleaning","False","","{site}","NodeId","ns=1;s=t|A_{UnitNumber}RunningForCleaning","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}RecycleParameters","RecycleOnTime","False","","{site}","NodeId","ns=1;s=t|{UnitNumber}RecycleOnTime","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}RecycleParameters","RecycleTimeSP","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}RecycleTimeSP","CyclicContinuous","Ti1s","None",""' + '\n'
            if "RecycleSampleParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}RecycleSampleParameters","AgitatorRunningForCleaning","False","","{site}","NodeId","ns=1;s=t|A_{UnitNumber}RunningForCleaning","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}RecycleSampleParameters","RecycleSmpTimeSp","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}RecycleSmpTimeSP","CyclicContinuous","Ti1s","None",""' + '\n'
            if "TransferToPackParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}TransferToPackParameters","FastFillFlowRate","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","InlineMixing","False","","{site}","NodeId","ns=1;s=t|ScratchBool","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","PackagingAdditiveQuantity","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","PackagingDestination","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}PackagingDestination","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","PackagingQuantity1","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}PackagingQuantity1","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","PackagingQuantity2","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}PackagingQuantity2","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","PackagingQuantity3","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}PackagingQuantity3","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","PackagingQuantity4","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}PackagingQuantity4","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","PigLineCode","0","","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","PressureSp","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","RecircFillFlowRate","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}TransferToPackParameters","SlowFillFlowRate","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
            if "WaitForAnalysisParameters" in PhasePar:
                anip = anip + f'WaitForAnalysisParameters","WaitForAnalysis","False","","{site}","NodeId","ns=1;s=t|{UnitNumber}WaitForAnalysis","CyclicContinuous","Ti1s","None",""' + '\n'
            if "DrainDrumParameters" in PhasePar:
                anip = anip + f'**Error** Drain drum Parameters not configured' + '\n'
            if "DoseFTParameters" in PhasePar:

                anip = anip + f'"{UnitNumber}DoseFTParameters","DosingDestination","0","","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}DoseFTParameters","ParFlowRateSp","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}DoseFTParameters","ParQueue","0","","{site}","NodeId","ns=1;s=t|*unknown_var*QUEUE","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}DoseFTParameters","ParSetPoint","0","","{site}","NodeId","ns=1;s=t|HFT_{unit_no_prefix}8_1SP","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}DoseFTParameters","RmName","0","","{site}","NodeId","ns=1;s=t|ScratchString","CyclicContinuous","Ti1s","None",""' + '\n'
            if "DoseParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}DoseParameters","DosingDestination","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}DoseParameters","ParSetPoint","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}DoseParameters","PressureSp","{site}","NodeId","ns=1;s=t|PIT_{unit_no_prefix}4_3SP","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}DoseParameters","RmName","{site}","NodeId","ns=1;s=t|{UnitNumber}RmName","CyclicContinuous","Ti1s","None",""' + '\n'
            if "FlushParameters" in PhasePar:
                anip = anip + f'**Error** Flush Parameters not configured' + '\n'
            if "GasBaDoseFTParameters" in PhasePar:
                anip = anip + f'**Error** GasBaDoseFTParameters not configured' + '\n'
            if "GasBaDoseParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}GasBaDoseParameters","BaMaxFlow","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}GasBaDoseParameters","BaMinFlow","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}GasBaDoseParameters","BaRampSlope","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}GasBaDoseParameters","DosingDestination","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}GasBaDoseParameters","FixedFlowSP","{site}","NodeId","ns=1;s=t|ScratchBool","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}GasBaDoseParameters","ParSetPoint","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}GasBaDoseParameters","PressureSp","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}GasBaDoseParameters","RmName","{site}","NodeId","ns=1;s=t|{UnitNumber}RmName","CyclicContinuous","Ti1s","None",""' + '\n'
            if "IFUReceiveParameters" in PhasePar:
                anip = anip + f'**Error** IFU Receive Parameters not configured' + '\n'
            if "MFUReceiveParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}MFUReceiveParameters","ContainerSp","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MFUReceiveParameters","ContainerType","0","","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MFUReceiveParameters","FillingLanceDrainTime","0","","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MFUReceiveParameters","FillToleranceDB","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MFUReceiveParameters","LabelNotNeeded","False","","{site}","NodeId","ns=1;s=t|ScratchBool","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MFUReceiveParameters","NrOfContainers","0","","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MFUReceiveParameters","PackagingQuantity","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}PackagingQuantity1","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MFUReceiveParameters","SlowContainerFillDB","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MFUReceiveParameters","User","0","","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
            if "MMMixingParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}MMMixingParameters","AtLeastOneBADosed","False","","{site}","NodeId","ns=1;s=t|ScratchBool","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MMMixingParameters","CylinderBAAddition","False","","{site}","NodeId","ns=1;s=t|ScratchBool","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MMMixingParameters","Destination","0","","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MMMixingParameters","FlowRate","0","","{site}","NodeId","ns=1;s=t|ScratchInt","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MMMixingParameters","MMOutletPressureSp","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MMMixingParameters","PackAdditiveQuantityPercent","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}MMMixingParameters","Source","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}Source","CyclicContinuous","Ti1s","None",""' + '\n'
            if "PiggingParameters" in PhasePar:
                anip = anip + f'**Error** Pigging Parameters not configured' + '\n'
            if "PremixerDoseParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}PremixerDoseParameters","PercentChangeFlowRate1","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}PremixerDoseParameters","PercentChangeFlowRate2","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}PremixerDoseParameters","TransferFlowRate1","0","","{site}","NodeId","ns=1;s=t|FT_1058_1SP1","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}PremixerDoseParameters","TransferFlowRate2","0","","{site}","NodeId","ns=1;s=t|FT_1058_1SP2","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}PremixerDoseParameters","TransferFlowRate3","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}PremixerDoseParameters","WeightChangeFlowRate","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}ChangeFlowWeight","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveByDSParameters" in PhasePar:
                anip = anip + f'**Error** Pigging Parameters not configured' + '\n'
            if "ReceiveFromMMParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}ReceiveFromMMParameters","CylinderRmName","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}CylinderRM","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveFromMMParameters","CylinderSetPoint","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveFromMMParameters","RmName","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}RMName","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveFromMMParameters","SetPoint","0","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveFromPremixerParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}ReceiveFromPremixerParameters","CriticalReaction","False","","{site}","NodeId","ns=1;s=t|{UnitNumber}CriticalReactionFlag","CyclicContinuous","Ti1s","None",""' + '\n'
                anip = anip + f'"{UnitNumber}ReceiveFromPremixerParameters","HypolProduction","False","","{site}","NodeId","ns=1;s=t|ScratchReal","CyclicContinuous","Ti1s","None",""' + '\n'
            if "ReceiveParallelParameters" in PhasePar:
                anip = anip + f'**Error** Receive Parallel Parameters not configured' + '\n'
            if "StartDoseFTParameters" in PhasePar:
                anip = anip + f'**Error** Start Dose FT Parameters not configured' + '\n'
            if "StartDoseWTParameters" in PhasePar:
                anip = anip + f'**Error** Start Dose WT Parameters not configured' + '\n'
            if "StopDoseFTParameters" in PhasePar:
                anip = anip + f'**Error** Stop Dose FT Parameters not configured' + '\n'
            if "StopDoseWTParameters" in PhasePar:
                anip = anip + f'**Error** Stop Dose WT Parameters not configured' + '\n'
            if "TLUReceiveParameters" in PhasePar:
                anip = anip + f'**Error** TLU Receive Parameters not configured' + '\n'
            if "TrDrumParameters" in PhasePar:
                anip = anip + f'**Error** Tr Drum Parameters not configured' + '\n'
            if "AddToRecLineParameters" in PhasePar:
                anip = anip + f'**Error** Add To Rec Line Parameters not configured' + '\n'
            if "DigestionParameters" in PhasePar:
                anip = anip + f'"{UnitNumber}DigestionParameter","DigestionTimeSP","0","","{site}","NodeId","ns=1;s=t|{UnitNumber}DigestionTime","CyclicContinuous","Ti1s","None",""' + '\n'
        else:
            anip = anip + f'No matching phase name for {PhasePar}. {UnitPhasePar} automation node instance not created \n'
    return anip