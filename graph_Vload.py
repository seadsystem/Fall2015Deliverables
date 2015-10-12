# Dominic Balassone
# graph_Vload.py
#
# END GOAL:
# takes in a csv file in the db.sead.systems format and outputs
# a matrix including the voltage readings
#
# CURRENTLY:
# reads in a file (fixed to split_rawax.csv for now) and creates
# a python matrix
#
# TODO:
# Allow user to designate file to input
# Graph these (unnecessary for API)

import numpy as np
import csv

#v_matrix will hold all the V(oltage) values from the file
v_matrix = []

#temp_reader will hold data directly from file in csv object
#QUOTE_NONE ignores quotes, for simplicity
temp_reader = csv.reader(open('split_rawax.csv','rb'), quoting=csv.QUOTE_NONE)

for row in temp_reader:
    # check for Volatage tag (V)
    row_data = next(temp_reader)
    if row_data[1] == 'V':
        v_matrix.append(row_data)

print(v_matrix)
