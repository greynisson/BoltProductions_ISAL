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

def find_index(char_level, index_pool, char_serie_indexes, letters, file):
        for index in index_pool:
            if len(char_serie_indexes) < char_level:

                new_char_serie_indexes = [char_index for char_index in char_serie_indexes]
                new_char_serie_indexes.append(index)

                new_index_pool = [index for index in index_pool]
                new_index_pool.remove(index)

                find_index(char_level, new_index_pool, new_char_serie_indexes, letters, file)

            else:
                word_incompleted = "".join([letters[i] for i in char_serie_indexes])
                chars_ending = "".join([letters[i] for i in index_pool])

                add_word(word_incompleted, chars_ending, file)
                break

def get_dashed_characters(letters):
    if len(letters) > 1:
        return letters.replace('','-')[1:-1]
    return letters