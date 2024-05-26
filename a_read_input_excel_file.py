import pandas as pd
import sys
import os

from z_logging_config import *

# Read the input file - ensure that the same file exists in this code directory
# xls = pd.ExcelFile('ANIInputFile.xlsx')
input_file = 'ANIInputFile.xlsx'
setup_logging()

class InputFileReader:

    def __init__(self, filename) -> None:
        self.filename = filename


    def is_file_exists(self):
        try:
            return os.path.isfile(input_file)
        except FileNotFoundError:
            logging.info(f"{input_file} does not exist.")
            print(f'The file {input_file} does not exist.')
            sys.exit(1)
        except Exception as e:
            print("An error occurred:", e)
            sys.exit(1)  # Exit the program with an error code

    def read_sheet(self, sheet_name):
        if self.is_file_exists():
            try:
                xls = pd.ExcelFile(self.filename)
                return pd.read_excel(xls, sheet_name)
            except Exception as e:
                print(f'The sheet "{sheet_name}" does not exist in file {self.filename}')
                print("An error occurred:", e)
                sys.exit(1)  # Exit the program with an error code


input_file_reader = InputFileReader(input_file)
