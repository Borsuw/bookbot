def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    word_counter = 0
    words = book_text.split()
    for word in words:
        word_counter +=1
    return word_counter

def count_characters(book_text):
    book_text_lower = book_text.lower()
    char_dict = {}
    for char in book_text_lower:
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] += 1
    return char_dict

def sort_key(item):
    return item[1]

def sort_char_dict(count_characters):
    char_dict = count_characters
    sorted_dicts = []
    dict_list = []
    for char, number in char_dict.items():
        if char.isalpha() == True:
            sorted_dicts.append((char, number))
    sorted_dicts.sort(reverse=True, key=sort_key)
    for char, number in sorted_dicts:
        dict_list.append({char: number})
    return dict_list