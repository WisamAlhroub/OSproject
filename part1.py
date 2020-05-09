import pandas as pd
import matplotlib.pyplot as plt
import threading, queue
from util.Preprocessor import *
import time
from PCB import *
from PageMapModel import *

# read the data and and put it in a table
information, table = read_data()
physical_mem_size, page_size, round_Q, CS = information
time_unit = 0.01

table = table.sort_values(by=['Arrival Time']).reset_index(drop=True)

frame_num = int(physical_mem_size / page_size)  # number of frame
ready_queue = []
# TODO start of part one of the project

q = queue.Queue()


def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        
        q.task_done()


threading.Thread(target=worker, daemon=True).start()
map_unit = PageMap(physical_mem_size, page_size)
i = 0
start_time = time.time()
for t in table["Arrival Time"].to_numpy():

    q.put(PCB(table["Process ID"][i], map_unit.add_process(table["Size in Bytes"][i]),
              time_in=time.time()))
    i += 1
    time.sleep(time_unit*t)
