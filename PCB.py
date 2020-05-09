class PCB:
    def __init__(self, process_id, page_table, state="ready",
                 time_in=None, time_out=None):
        self.process_id = process_id
        self.page_table = page_table
        self.state = state
        self.time_in = time_in
        self.time_out = time_out
