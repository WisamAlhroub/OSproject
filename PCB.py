class PCB:
    def __init__(self, process_id, page_table, page_num, state="ready",
                 num_page_swap=0, time_in=None, time_out=None):
        self.process_id = process_id
        self.page_table = page_table
        self.page_num = page_num
        self.state = state
        self.num_page_swap = num_page_swap
        self.time_in = time_in
        self.time_out = time_out
