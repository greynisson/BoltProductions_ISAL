from timeit import default_timer as timer
from classes import Bolts
from functions import * #reverse, get_process_time, assign_machine_1, assign_machine_2, inverse_binary
import csv

start = timer()
data = Bolts(True)
machine_1 = Bolts(False)
machine_2 = Bolts(False)
max_iterations = 1
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
        
data.total_time()

while len(tested_binary) < max_iterations:
    best_binary = ""
    time_difference = data.processing_time
    for i in range(0,pow(2,data.mould_types)):
        machine_1.binary = reverse(i, data.mould_types)
        time1 = get_process_time(machine_1.binary, data.casting_time)
        time2 = data.processing_time - time1
        if abs(time1 - time2) < time_difference:
            if machine_1.binary not in tested_binary and inverse_binary(machine_1.binary) not in tested_binary:
                machine_2.binary = inverse_binary(machine_1.binary)
                time_difference = abs(time1 - time2)
                machine_1.make_schedule(data)
                machine_2.make_schedule(data)
                machine_1.total_time()
                machine_2.total_time()
                best_binary = machine_1.binary

    tested_binary.append(best_binary)
    
    print_mould_schedule(machine_1, machine_2, time_difference, len(tested_binary))
    
stop = timer()
result = stop - start
print(f"Time 1: {result}")