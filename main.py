import sys
from stats import get_book_text, count_words, count_characters, sort_char_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <relative path to book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_list = sort_char_dict(count_characters(book_text))
    print(f"============ BOOKBOT ============\n"
          f"Analyzing book found at {book_path}\n"
          f"------------ Word Count ------------\n"
          f"Found {word_count} total words\n"
          f"------------ Character Count ------------")
    for char_dict in char_list:
        char, number = list(char_dict.items())[0]
        print(f"{char}: {number}")
    print("============ END ============")

main()