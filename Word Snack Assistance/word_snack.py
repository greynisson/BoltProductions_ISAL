def sort_word(word):
    char_array = []
    for char in word:
        char_array.append(char)
    char_array.sort()
    sorted_word = "".join(char_array)
    return sorted_word

def add_word(current_string, next_chars, file):
    for next_char in next_chars:
        file.write(current_string + next_char + "\n")

def find_index(index_pool, serie, letters, file):
        for index in index_pool:
            if len(serie) < level:
                new_serie = []
                new_index_pool = []
                for s in serie: new_serie.append(s)
                for i in index_pool: new_index_pool.append(i)
                new_serie.append(index)
                new_index_pool.remove(index)
                find_index(new_index_pool, new_serie, letters, file)
            else:
                word = ""
                chars = ""
                for s in serie: word += letters[s]
                for i in index_pool: chars += letters[i]
                add_word(word, chars, file)
                break
                
from timeit import default_timer as timer

start = timer()

#input_string = "NANURGB"
input_string = input("Enter your characters:")
letters = sort_word(input_string.upper())
print(letters)
level = 0
serie = []
index_pool = list(range(0,len(letters)))

f = open("word_snack_results.txt", "w")

while level < len(input_string):
    find_index(index_pool, serie, letters, f)
    level += 1

f.close()

print(f"Runtime: {timer() - start}")



"""
def make_word(letters):
    chars = []
    for letter in letters:
        chars.append(letter)
    chars.sort()
    return chars

def print_word(word, chars):
    for char in chars:
        new_word = "".join(word) + char
        print(new_word)

def find_index(i, limit):
    if len(i) < limit:
        arr.append(i)
        return find_word(arr, char, chars, limit)
    else:
        for c in chars:
            print_word(arr,c)
        chars = make_word(word)

def write_word(word, chars, file):
    for char in chars:
        new_word = "".join(word) + char
        file.write(new_word + "\n")



def stuff(chars, word, level, letters, f):
    isDone = False
    if level > 0:
        for letter in chars:
            if not isDone:
                if len(word) < level:
                    new_word = []
                    new_chars = []
                    for w in word: new_word.append(w)
                    for c in chars: new_chars.append(c)
                    new_word.append(letter)
                    new_chars.remove(letter)
                    stuff(new_chars, new_word, level, letters, f)
                else:
                    add_word(word, chars, f)
                    #write_word(word, chars, f)
                    isDone = True
                
    else:
        add_word(word, chars, f)
        #write_word(word, chars, f)

chars = make_word(letters)
word = []
"""