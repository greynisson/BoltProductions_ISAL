class Machine:

    processing_time = 0
    mould_types = 0
    binary = ""

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= self.mould_types - 1:
            raise StopIteration
        index = self.index
        self.index += 1
        return self.casting_time[index]

    
    def __init__(self, is_total):
        self.id = {}
        self.quantity = []
        self.casting_time = []
        self.mould = []
        self.is_total = is_total
        self.index = 0
        self.schedule = {}
        if is_total:
            input_filename ='Data/alloys.txt'
            alloy_indices = {}
            with open(input_filename, newline='') as file:
                line = file.readline().strip()
                while line:
                    data = line.split(",")
                    mould_size = data[0]
                    indices = ""
                    if len(data[1]) > 0:
                        indices += "0"
                        for alloy in data[1:]:
                            if len(alloy) > 1:
                                alloy_info = alloy.split("-")
                                alloy_index = alloy_info[0]
                                alloy_quantity = int(alloy_info[1])
                                for i in range(0, alloy_quantity):
                                    indices += alloy_index
                        alloy_indices[mould_size] = indices
                    line = file.readline().strip()

            self.schedule = alloy_indices


    def get_process_time(self):
        mould_exchange = -1
        casting_time = 0
        exchange_time = 30
        binary = self.binary
        for j in range(0,len(binary)):
            if binary[j] == "1":
                casting_time += self.casting_time[j]
        for mould in binary:
            mould_exchange += int(mould)
        self.processing_time = casting_time + exchange_time * mould_exchange


    
    def make_schedule(self, data):
        casting_time = []
        mould = []
        quantity = []
        schedule = {}
        i = 0
        for b in self.binary:
            if b == "1":
                mould.append(data.mould[i])
                quantity.append(data.quantity[i])
                schedule[data.mould[i]] = data.schedule[data.mould[i]]
            i += 1
        self.casting_time = casting_time
        self.mould = mould
        self.quantity = quantity
        self.schedule = schedule


