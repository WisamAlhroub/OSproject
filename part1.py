import pandas as pd
import matplotlib.pyplot as plt
from util.Preprocessor import *
from PageMapModel import *

# read the data and and put it in a table
information, table = read_data()
physical_mem_size, page_size, round_Q, CS = information


table = table.sort_values(by=['Arrival Time']).reset_index(drop=True)

frame_num = int(physical_mem_size/page_size) # number of frame
ready_queue = []
# TODO start of part one of the project

