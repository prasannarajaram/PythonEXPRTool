# TODO Remove millisecond from the logging output.

import os
from datetime import datetime
import pdb

from z_logging_config import *

def delete_prev_output_file(output_file):
    # Check if the file exists
    setup_logging()
    if os.path.exists(output_file):
        # Attempt to delete the file
        os.remove(output_file)
        logging.info(f"{output_file} has been deleted.")
    else:
        logging.info(f"{output_file} not found. New file will be created once the scipt is complete")