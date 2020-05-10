import pandas as pd
import matplotlib.pyplot as plt
import threading, queue
from util.Preprocessor import *
import time
from PCB import *
from PageMapModel import *
from util.const import *

# read the data and and put it in a table
information, table = read_data()
physical_mem_size, page_size, round_Q, CS = information
time_unit = 0.1
start_time = None
table = table.sort_values(by=['Arrival Time']).reset_index(drop=True)

frame_num = int(physical_mem_size / page_size)  # number of frame
ready_queue = []
# TODO start of part one of the project

q = queue.Queue()


def worker():
    while True:
        item = q.get()
        print(OKBLUE + f'Working on {item.process_id}' + ENDC)
        wating_time = table[table["Process ID"] == item.process_id]["CPU Burst"].item()
        time.sleep(time_unit * wating_time)
        print(OKGREEN + f'Finished {item.process_id} at {time.time() - start_time}' + ENDC)
        map_unit.remove_process(item.page_table)
        q.task_done()
        time.sleep(CS * time_unit)


threading.Thread(target=worker, daemon=True).start()
map_unit = PageMap(physical_mem_size, page_size)
i = 0
start_time = time.time()
for t in table["Arrival Time"].to_numpy():

    q.put(PCB(table["Process ID"][i], map_unit.add_process(table["Size in Bytes"][i]),
              time_in=time.time()))

    wait = 0
    if i != table.shape[0] - 1:
        wait = table["Arrival Time"][i + 1] - t
    print(f'Arrival Time of {table["Process ID"][i]} : ', time.time() - start_time)
    i += 1
    time.sleep(time_unit * wait)
print(HEADER + "done" + ENDC)
