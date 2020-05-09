import pandas as pd
import matplotlib.pyplot as plt
from util.Preprocessor import *

# read the data and and put it in a table
information, table = read_data()
physical_mem_size, page_size, round_Q, CS = information

# TODO sort the data by Arrival Time to make the table suitable for pressing
table = table.sort_values(by=['Arrival Time'])

frame_num = int(physical_mem_size/page_size) # number of frame
ready_queue = []

for i in range(table.size):