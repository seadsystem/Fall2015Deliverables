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
# Only add voltage (V) readings to the matrix
# Graph these (unnecessary for API)

import numpy as np

my_matrix = []
for line in open('split_rawax.csv'):
    temp_matrix = line.split()
    my_matrix.append(temp_matrix)

my_matrix
