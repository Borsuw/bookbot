from stats import get_book_text, count_words, count_characters

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    print(f"{word_count} words found in the document")
    print(char_count)

main()