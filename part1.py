import pandas as pd
import matplotlib.pyplot as plt
from util.Preprocessor import *

# read the data and and put it in a table
information, table = read_data()
physical_mem_size, page_size, round_Q, CS = information

# TODO sort the data by Arrival Time to make the table suitable for pressing
