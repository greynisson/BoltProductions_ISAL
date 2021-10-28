from timeit import default_timer as timer
from word_snack_functions import * # sort_word, find_index, get_dashed_characters

char_level = 0
char_serie = []
file_results = open("word_snack_results.txt", "w")

#input_string = "NANURGB"
input_string = input("Enter your characters:")

start_time = timer()
letters = sort_word(input_string.upper())
index_pool = list(range(0,len(letters)))

print(f"Character-pool: {get_dashed_characters(letters)}")

while char_level < len(input_string):
    find_index(char_level, index_pool, char_serie, letters, file_results)
    char_level += 1

file_results.close()

end_time = round(timer() - start_time, 3)

print(f"Runtime: {end_time} seconds.")