from stats import get_book_text, count_words, count_characters, sort_char_dict

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_list = sort_char_dict(count_characters(book_text))
    print(f"============ BOOKBOT ============\n"
          f"Analyzing book found at {book_path}\n"
          f"----------- Word Count ----------\n"
          f"Found {word_count} total words\n"
          f"--------- Character Count -------")
    for char_dict in char_list:
        for char, number in char_dict.items():
            print(f"{char}: {number}")
    print("============= END ===============")

main()