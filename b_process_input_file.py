import pdb
from a_read_input_excel_file import *

def process_units_phases():
    units_phases = input_file_reader.read_sheet('UnitsPhases')
    # Remove leading Ph in every phase name
    # pdb.set_trace()
    units_phases['PhaseNames'] = units_phases['PhaseNames'].str[2:]

    # Removes the trailing 1 or 2 or 3 from the phase name
    units_phases['PhaseNames'] = units_phases['PhaseNames'].str.rstrip('123')

    # Removes the duplicates (in-place) after removing the trailing 1 or 2 or 3
    units_phases.drop_duplicates(inplace=True)

    # extract the unit number and phase name from the PhaseNames column
    ## the below regex will
    pattern = r'(\w+\d+)(\w+)'
    unit_phase_extract = units_phases['PhaseNames'].str.extract(pattern)
    unit_phase_extract.columns = ['Unit', 'Phase']
    return unit_phase_extract

def process_generic_storage_tanks():
    '''Convert the generic tank names into list and pass it on to automation node instance'''
    storage_tanks = input_file_reader.read_sheet('GenericStorageTank')
    storage_tanks_list = storage_tanks["GenericStorageTankNames"].tolist()
    return storage_tanks_list


def process_generic_blender():
    '''Convert the generic blender names into list and pass it on to automation node instance'''
    generic_blender = input_file_reader.read_sheet('GenericBlender')
    generic_blender_list = generic_blender["GenericBlenderNames"].tolist()
    return generic_blender_list


def process_generic_manual_unit():
    '''Convert the generic manual unit names into list and pass it on to automation node instance'''
    generic_manual_unit = input_file_reader.read_sheet('GenericManualUnit')
    generic_manual_unit_list = generic_manual_unit["GenericManualUnitNames"].tolist()
    return generic_manual_unit_list


def process_generic_premixer():
    '''Convert the generic premixer names into list and pass it on to automation node instance'''
    generic_premixer = input_file_reader.read_sheet('GenericPremixer')
    generic_premixer_list = generic_premixer["GenericPremixerNames"].tolist()
    return generic_premixer_list


def process_generic_reactor():
    '''Convert the generic manual unit names into list and pass it on to automation node instance'''
    generic_reactor = input_file_reader.read_sheet('GenericReactor')
    generic_reactor_list = generic_reactor["GenericReactorNames"].tolist()
    return generic_reactor_list


def process_generic_repackaging():
    '''Convert the generic premixer names into list and pass it on to automation node instance'''
    generic_repackaging = input_file_reader.read_sheet('GenericRePackaging')
    generic_repackaging_list = generic_repackaging["GenericRepackagingNames"].tolist()
    return generic_repackaging_list