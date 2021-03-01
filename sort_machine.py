from timeit import default_timer as timer
from classes import Machine
from functions import * 
import csv

start = timer()
data = Machine(True)
machine_1 = Machine(False)
machine_2 = Machine(False)
max_iterations = 3
max_moulds = 0
tested_binary = []

with open('Data/bolts.csv', newline='') as csvfile:
     dataset = csv.reader(csvfile)
     for row in dataset:
         size = row[0]
         casting_time = int(row[1])
         quantity = int(row[3])
         
         if quantity:
             data.quantity.append(quantity)
             data.casting_time.append(quantity * casting_time)
             data.mould.append(size)
             max_moulds += 1

data.total_time()

while len(tested_binary) < max_iterations:
    best_binary = ""
    best_time_difference = data.processing_time
    for i in range(0, pow(2, max_moulds)):
        mould_binary = get_binary_sequence(i, max_moulds)
        time1 = data.get_process_time(mould_binary)
        time2 = data.processing_time - time1
        if abs(time1 - time2) < best_time_difference:
            if mould_binary not in tested_binary and inverse_binary(mould_binary) not in tested_binary:
                machine_1.binary = mould_binary
                machine_2.binary = inverse_binary(mould_binary)
                machine_1.make_schedule(data)
                machine_2.make_schedule(data)
                machine_1.total_time()
                machine_2.total_time()
                best_binary = mould_binary
                best_time_difference = abs(time1 - time2)

    tested_binary.append(best_binary)
    print_mould_schedule(machine_1, machine_2, best_time_difference, len(tested_binary))
    make_mould_sequence(machine_1.schedule, {})
    
stop = timer()
result = stop - start
print(f"Time 1: {result}")


