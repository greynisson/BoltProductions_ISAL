class Bolts:

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

    
    def __init__(self, isTotal):
        self.id = {}
        self.quantity = []
        self.casting_time = []
        self.mould = []
        self.isTotal = isTotal
        self.index = 0
    
    def total_time(self):
        self.mould_types = len(self.casting_time)
        exchange_time = 0
        casting_time = sum(self.casting_time)
        if self.isTotal:
            exchange_time = 30 * (self.mould_types - 2)
        else: 
            exchange_time = 30 * (self.mould_types - 1)
        self.processing_time = exchange_time + casting_time

    
    def make_schedule(self, data):
        casting_time = []
        mould = []
        quantity = []
        i = 0
        word = ""
        for b in self.binary:
            if b == "1":
                casting_time.append(data.casting_time[i])
                mould.append(data.mould[i])
                quantity.append(data.quantity[i])
            i += 1
        self.casting_time = casting_time
        self.mould = mould
        self.quantity = quantity

