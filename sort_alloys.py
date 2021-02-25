from functions import *

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
    # Myndum vilja sækja alloy_combinations í einverja skrá / gagnagrunn

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


data = {'203': ['0'], '215': ['0', '5'], '305': ['0', '1', '1']}
mould_array = ['203', '215', '305']
data2 = {'178': ['0'], '228': ['0', '4'], '254': ['0', '2', '2', '2', '3', '4'],  '279': ['0']}
mould_array2 = ['178', '228', '254', '279']

alloy_indices = make_alloy_indices()
alloy_indices_m1 = {}

for mould in mould_array2:
    alloy_indices_m1[mould] = alloy_indices[mould]

#print(alloy_indices)

make_mould_sequence(alloy_indices_m1, {})

"""
moulds = ['305', '203']
first_mould = moulds[0]
data = {'203': ['0'], '215': ['0', '5'], '305': ['0', '1', '1']}
first_alloys = data[first_mould]

make_alloy_sequence(first_alloys, moulds, data, [], {})

moulds2 = ['215', '203']
first_mould2 = moulds2[0]
data2 = {'203': ['0'], '215': ['0', '5'], '305': ['0', '1', '1']}
first_alloys2 = data2[first_mould2]
print("Next")
make_alloy_sequence(first_alloys2, moulds2, data2, [], {})

def verify_production_plan(production_sequence):
    is_valid = True
    alloy_combinations = {"0": "023", "1": "013", "2": "45", "3": "45", "4": "35", "5": "04"}
    #production_sequence = "024350"

    for i in range(0, len(production_sequence) - 1):
        first_alloy = production_sequence[i]
        second_alloy = production_sequence[i+1]
        print(f"Alloys: {first_alloy} ---> {second_alloy}")
        if second_alloy in alloy_combinations[first_alloy]:
            print(f"{second_alloy} is in {alloy_combinations[first_alloy]}")
        else:
            print(f"{second_alloy} is not in {alloy_combinations[first_alloy]}")
            is_valid = False
            break

    if is_valid:
        print("This production sequence is valid.")
    else:
        print("This production sequence is not valid.")

    return is_valid
"""