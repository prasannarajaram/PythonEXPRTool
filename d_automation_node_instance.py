from b_process_input_file import *

def create_automation_node_instance(site):
    '''Create Automation Node Instance'''
    storage_tanks_list = process_generic_storage_tanks()
    ani = ''
    if storage_tanks_list:
        for tank in storage_tanks_list:
            ani = ani + f'"Employable","{tank}Employable","","","{site}"' + '\n'
            ani = ani + f'"GenericStorageTank","{tank}","","","{site}"' + '\n'
    else:
        print("No tanks found")
        # logging.info(f"No storage tanks found.")

    generic_blender_list = process_generic_blender()
    if generic_blender_list:
        for generic_blender in generic_blender_list:
            ani = ani + f'"GenericBlender","{generic_blender}","","","{site}"'  + '\n'

    generic_manual_unit_list = process_generic_manual_unit()
    if generic_manual_unit_list:
        for generic_manual_unit in generic_manual_unit_list:
            ani = ani + f'"GenericManualUnit","{generic_manual_unit}","","","{site}"' + '\n'

    generic_premixer_list = process_generic_premixer()
    if generic_premixer_list:
        for generic_premixer in generic_premixer_list:
            ani = ani + f'"GenericPremixer","{generic_premixer}","","","{site}"' + '\n'

    generic_reactor_list = process_generic_reactor()
    if generic_reactor_list:
        for generic_reactor in generic_reactor_list:
            ani = ani + f'"GenericReactor","{generic_manual_unit}","","","{site}"' + '\n'

    generic_repackaging_list = process_generic_repackaging()
    if generic_repackaging_list:
        for generic_repackaging in generic_repackaging_list:
            ani = ani + f'"GenericRepackaging","{generic_repackaging}","","","{site}"' + '\n'

    units_phases = process_units_phases()
    if not units_phases.empty:
        units_phases["PhasePar"] = units_phases["Phase"] + 'Parameters'
        units_phases["PhaseRep"] = units_phases["Phase"] + 'Report'
        units_phases["UnitPhasePar"] = units_phases["Unit"] + units_phases["PhasePar"]
        units_phases["UnitPhaseRep"] = units_phases["Unit"] + units_phases["PhaseRep"]
        for PhasePar, UnitPhasePar in zip(units_phases["PhasePar"].tolist(), units_phases["UnitPhasePar"].tolist()):
            parameter_typicals = ["DrainParameters", "MixParameters", "ReceiveByFTParameters", "ReceiveByWTParameters",
                                "ReceiveFromDrumParameters", "RecycleParameters", "RecycleSampleParameters",
                                "TransferToPackParameters", "WaitForAnalysisParameters", "DrainDrumParameters",
                                "DoseFTParameters", "DoseParameters", "FlushParameters", "GasBaDoseFTParameters",
                                "GasBaDoseParameters", "IFUReceiveParameters", "MFUReceiveParameters",
                                "MMMixingParameters", "PiggingParameters", "PremixerDoseParameters", "ReceiveByDSParameters",
                                "ReceiveFromMMParameters", "ReceiveFromPremixerParameters", "ReceiveParallelParameters" ,
                                "StartDoseFTParameters", "StartDoseWTParameters", "StopDoseFTParameters", "StopDoseWTParameters",
                                "TLUReceiveParameters", "TrDrumParameters", "AddToRecLineParameters", "DigestionParameters"]
            if PhasePar in parameter_typicals:
                if "DrainParameters" in PhasePar:
                    ani = ani + f'"DrainParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "MixParameters" in PhasePar:
                    ani = ani + f'"MixParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "ReceiveByFTParameters" in PhasePar:
                    ani = ani + f'"ReceiveByFTParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "ReceiveByWTParameters" in PhasePar:
                    ani = ani + f'"ReceiveByWTParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "ReceiveFromDrumParameters" in PhasePar:
                    ani = ani + f'"ReceiveFromDrumParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "RecycleParameters" in PhasePar:
                    ani = ani + f'"RecycleParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "RecycleSampleParameters" in PhasePar:
                    ani = ani + f'"RecycleSampleParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "TransferToPackParameters" in PhasePar:
                    ani = ani + f'"TransferToPackParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "WaitForAnalysisParameters" in PhasePar:
                    ani = ani + f'"WaitForAnalysisParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "DrainDrumParameters" in PhasePar:
                    ani = ani + f'""DrainDrumParameters,"{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "DoseFTParameters" in PhasePar:
                    ani = ani + f'"DoseFTParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "DoseParameters" in PhasePar:
                    ani = ani + f'"DoseParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "FlushParameters" in PhasePar:
                    ani = ani + f'"FlushParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "GasBaDoseFTParameters" in PhasePar:
                    ani = ani + f'"GasBaDoseFTParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "GasBaDoseParameters" in PhasePar:
                    ani = ani + f'"GasBaDoseParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "IFUReceiveParameters" in PhasePar:
                    ani = ani + f'"IFUReceiveParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "MFUReceiveParameters" in PhasePar:
                    ani = ani + f'"MFUReceiveParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "MMMixingParameters" in PhasePar:
                    ani = ani + f'"MMMixingParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "PiggingParameters" in PhasePar:
                    ani = ani + f'"PiggingParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "PremixerDoseParameters" in PhasePar:
                    ani = ani + f'"PremixerDoseParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "ReceiveByDSParameters" in PhasePar:
                    ani = ani + f'"ReceiveByDSParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "ReceiveFromMMParameters" in PhasePar:
                    ani = ani + f'"ReceiveFromMMParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "ReceiveFromPremixerParameters" in PhasePar:
                    ani = ani + f'"ReceiveFromPremixerParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "ReceiveParallelParameters" in PhasePar:
                    ani = ani + f'"ReceiveParallelParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "StartDoseFTParameters" in PhasePar:
                    ani = ani + f'"StartDoseFTParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "StartDoseWTParameters" in PhasePar:
                    ani = ani + f'"StartDoseWTParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "StopDoseFTParameters" in PhasePar:
                    ani = ani + f'"StopDoseFTParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "StopDoseWTParameters" in PhasePar:
                    ani = ani + f'"StopDoseWTParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "TLUReceiveParameters" in PhasePar:
                    ani = ani + f'"TLUReceiveParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "TrDrumParameters" in PhasePar:
                    ani = ani + f'"TrDrumParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "AddToRecLineParameters" in PhasePar:
                    ani = ani + f'"AddToRecLineParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
                if "DigestionParameters" in PhasePar:
                    ani = ani + f'"DigestionParameters","{UnitPhasePar}","{UnitPhasePar}","","{site}"' + '\n'
            else:
                ani = ani + f'**Error** No matching phase name for {PhasePar}. {UnitPhasePar} automation node instance not created \n'

        for PhaseRep, UnitPhaseRep in zip(units_phases["PhaseRep"].tolist(), units_phases["UnitPhaseRep"].tolist()):
            report_typicals = ["AddToRecLineReport", "DigestionReport", "DoseFTReport", "DoseReport",
                            "DrainDrumReport", "DrainFromMMReport", "DrainReport", "FlushReport",
                            "GasBaDoseFTReport", "GasBaDoseReport", "IFUReceiveReport", "MFUReceiveReport",
                            "PiggingReport", "PremixerDoseReport", "ReceiveByDSReport", "ReceiveByFTReport",
                            "ReceiveByWTReport", "ReceiveFromDrumReport", "ReceiveFromMMReport", "ReceiveParallelReport",
                            "RecycleReport", "RecycleSampleReport", "StopDoseFTReport", "StopDoseWTReport",
                            "TLUReceiveReport", "TransferToPackReport", "TrDrumReport", "WaitForAnalysisReport"]
            if PhaseRep in report_typicals:
                if "AddToRecLineReport" in PhaseRep:
                    ani = ani + f'"AddToRecLineReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "MixReport" in PhaseRep:
                    pass
                if "DigestionReport" in PhaseRep:
                    ani = ani + f'"DigestionReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "DoseFTReport" in PhaseRep:
                    ani = ani + f'"DoseFTReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "DoseReport" in PhaseRep:
                    ani = ani + f'"DoseReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "DrainDrumReport" in PhaseRep:
                    ani = ani + f'"DrainDrumReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "DrainFromMMReport" in PhaseRep:
                    ani = ani + f'"DrainFromMMReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "DrainReport" in PhaseRep:
                    ani = ani + f'"DrainReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "FlushReport" in PhaseRep:
                    ani = ani + f'"FlushReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "GasBaDoseFTReport" in PhaseRep:
                    ani = ani + f'"GasBaDoseFTReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "GasBaDoseReport" in PhaseRep:
                    ani = ani + f'"GasBaDoseReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "IFUReceiveReport" in PhaseRep:
                    ani = ani + f'"IFUReceiveReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "MFUReceiveReport" in PhaseRep:
                    ani = ani + f'"MFUReceiveReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "PiggingReport" in PhaseRep:
                    ani = ani + f'"PiggingReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "PremixerDoseReport" in PhaseRep:
                    ani = ani + f'"PremixerDoseReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "ReceiveByDSReport" in PhaseRep:
                    ani = ani + f'"ReceiveByDSReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "ReceiveByFTReport" in PhaseRep:
                    ani = ani + f'"ReceiveByFTReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "ReceiveByWTReport" in PhaseRep:
                    ani = ani + f'"ReceiveByWTReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "ReceiveFromDrumReport" in PhaseRep:
                    ani = ani + f'"ReceiveFromDrumReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "ReceiveFromMMReport" in PhaseRep:
                    ani = ani + f'"ReceiveFromMMReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "ReceiveParallelReport" in PhaseRep:
                    ani = ani + f'"ReceiveParallelReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "RecycleReport" in PhaseRep:
                    ani = ani + f'"RecycleReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "RecycleSampleReport" in PhaseRep:
                    ani = ani + f'"RecycleSampleReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "StopDoseFTReport" in PhaseRep:
                    ani = ani + f'"StopDoseFTReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "StopDoseWTReport" in PhaseRep:
                    ani = ani + f'"StopDoseWTReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "TLUReceiveReport" in PhaseRep:
                    ani = ani + f'"TLUReceiveReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "TransferToPackReport" in PhaseRep:
                    ani = ani + f'"TransferToPackReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "TrDrumReport" in PhaseRep:
                    ani = ani + f'"TrDrumReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
                if "WaitForAnalysisReport" in PhaseRep:
                    ani = ani + f'"WaitForAnalysisReport","{UnitPhaseRep}","{UnitPhaseRep}","","{site}"' + '\n'
            else:
                ani = ani + f'**Error** No matching phase name for {PhaseRep}. {UnitPhaseRep} automation node instance not created \n'
    return ani