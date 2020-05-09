import numpy as np
import pandas as pd


class PageMap:

    def __init__(self, physical_mem_size, page_size):
        self.physical_mem_size = physical_mem_size
        self.page_size = page_size

        # frames in the physical memory
        self.frames = np.arange(int(physical_mem_size / page_size))
        self.frame_state = np.zeros(self.frames.size)
        self.frame_value = np.zeros(self.frames.size)

    def add_process(self, process_size):
        process_page_num = int(process_size / self.page_size)
        process_page = np.arange(process_page_num)
        num_free_frames = (self.frame_state == 0).size

        np.random.shuffle(process_page)
        map_page = (self.frames[self.frame_state == 0])
        self.frame_value[self.frame_state == 0] = process_page[:num_free_frames]

        if process_page_num > num_free_frames:
            map_page += (['HDD'] * int(process_page_num - num_free_frames))

        page_table = {
            'page-number': np.array(process_page).astype(int),
            'map-value': np.array(map_page),
            'valid-invalid': np.array(map_page) != 'HDD'
        }

        return pd.DataFrame(page_table).sort_values(by='page-number')
