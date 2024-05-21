#!/usr/bin/python3
import pdb
import pandas as pd
import re

from a_read_input_excel_file import *
from b_process_input_file import *
from c_six_bit_task import *
from d_automation_node_instance import *
from e_automation_node_instance_par import *
from f_automation_node_instance_rep import *
from g_write_to_file import *
from h_delete_old_output_file import *

site = 'DILOVASI'
output_file = 'output.txt'

def main():
    delete_prev_output_file(output_file)
    write_to_output_file(create_sbt(site),output_file)
    write_to_output_file(create_automation_node_instance(site), output_file)
    write_to_output_file(create_automation_node_instance_par(site), output_file)
    write_to_output_file(create_automation_node_instance_rep(site), output_file)

if __name__ == '__main__':
    main()
