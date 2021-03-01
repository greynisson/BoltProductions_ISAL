def get_binary_sequence(number, N):
    binary = bin(number)[2:]
    new_binary = binary[::-1]
    counter = len(binary)
    while counter < N:
        new_binary += "0"
        counter += 1
    return new_binary


def get_process_time(active_moulds, times):
    mould_exchange = -1
    casting_time = 0
    for j in range(0,len(active_moulds)):
        if active_moulds[j] == "1": casting_time += times[j]
    for mould in active_moulds:
        mould_exchange += int(mould)
    return casting_time + 30 * mould_exchange


def inverse_binary(binary):
    new_binary = ""
    for b in binary:
        if b == "1": new_binary += "0"
        else: new_binary += "1"
    return new_binary


def make_alloy_indices():
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

    return alloy_indices

def make_mould_sequence(alloy_indices, production_data):
    for alloy_index in alloy_indices:
        i = alloy_index
        current_production_data = production_data.copy()
        current_production_data[i] = list(alloy_indices[i])
        new_alloy_indices = alloy_indices.copy()
        new_alloy_indices.pop(i)
        if new_alloy_indices:
            make_mould_sequence(new_alloy_indices, current_production_data)
        else:
            moulds = list(current_production_data.keys())
            first_mould = moulds[0]
            first_alloys = current_production_data[first_mould]
            
            make_alloy_sequence(first_alloys, moulds, current_production_data, [], {}, "")


def make_alloy_sequence(alloys, moulds, data, sequence, production_plan, production_sequence):
    for alloy in alloys:
        remaining_alloys = [c for c in alloys]
        updated_sequence = [w for w in sequence]
        remaining_alloys.remove(alloy)
        updated_sequence.append(alloy)
    
        if remaining_alloys: 
            make_alloy_sequence(remaining_alloys, moulds, data, updated_sequence, production_plan, production_sequence)
                
        else:
            updated_production_sequence = ""
            for alloy in production_sequence: updated_production_sequence += alloy
            production_plan[moulds[0]] = updated_sequence
            for alloy in updated_sequence: updated_production_sequence += alloy
            remaining_moulds = [m for m in moulds]
            remaining_moulds.pop(0)
            if remaining_moulds:
                next_mould = remaining_moulds[0]
                next_alloys = data[next_mould]
                make_alloy_sequence(next_alloys, remaining_moulds, data, [], production_plan, updated_production_sequence)
                del next_alloys, remaining_moulds
            else:
                if verify_production_plan(updated_production_sequence):
                    production_string = ""
                    for mould in list(production_plan.keys()):
                        production_string += (mould + ": ")
                        alloy_array = []
                        for alloy in list(production_plan[mould]):
                            alloy_array.append(alloy)
                        production_string += ",".join(alloy_array) + " "
                        
                    print(production_string)

def verify_production_plan(production_sequence):
    is_valid = True
    alloy_combinations = {"0": "012", "1": "15", "2": "24", "3": "23", "4": "034", "5": "05"}
    # Myndum vilja eiga möguleika á að sækja alloy_combinations í einverja skrá / gagnagrunn

    if (production_sequence.startswith('0') * production_sequence.endswith('0')):

        for i in range(0, len(production_sequence) - 1):
            first_alloy = production_sequence[i]
            second_alloy = production_sequence[i+1]

            if second_alloy not in alloy_combinations[first_alloy]:
                is_valid = False
                break

    else:
        return False     
            
    return is_valid


def print_mould_schedule(machine_1, machine_2, best_time_difference, iteration):
    print(f"**************** Iteration {iteration} ***************")
    print(f"Machine 1: {machine_1.mould}")
    print(f"Machine 2: {machine_2.mould}")
    print(f"Time difference: {best_time_difference}")
    print(f"Casting machine 1: {machine_1.processing_time} min")
    print(f"Casting machine 2: {machine_2.processing_time} min")
    #print(f"Times: {data.casting_time}")
    print(f"********************************************")
    print("")