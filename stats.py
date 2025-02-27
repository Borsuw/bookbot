def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    counter = 0
    words = book_text.split()
    for word in words:
        counter +=1
    return counter