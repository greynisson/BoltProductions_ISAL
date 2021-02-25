from functions import *




data = {'203': ['0'], '215': ['0', '5'], '305': ['0', '1', '1']}
mould_array = ['203', '215', '305']
data2 = {'178': ['0'], '228': ['0', '4'], '254': ['0', '2', '2', '2', '3', '4'],  '279': ['0']}
mould_array2 = ['178', '228', '254', '279']

alloy_indices = make_alloy_indices()
alloy_indices_m1 = {}

for mould in mould_array2:
    alloy_indices_m1[mould] = alloy_indices[mould]

print(alloy_indices)

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