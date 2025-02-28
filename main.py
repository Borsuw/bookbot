import sys
from stats import get_book_text, count_words, count_characters, sort_char_dict

def generate_report(book_path, word_count, char_list):
    report = (f"============ BOOKBOT ============\n"
              f"Analyzing book found at {book_path}\n"
              f"------------ Word Count ------------\n"
              f"Found {word_count} total words\n"
              f"------------ Character Count ------------\n")
    for char_dict in char_list:
        char, number = list(char_dict.items())[0]
        report += f"{char}: {number}\n"
    report += "============ END ============\n"
    return report

def write_report(report):
    with open("report.txt", "w") as f:
        f.write(report)
    print("Output written to report.txt, exiting...")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <relative path to book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_list = sort_char_dict(count_characters(book_text))
    report = generate_report(book_path, word_count, char_list)
    print(report)
    print("Would you like to print the output to a file? (y/n)")
    user_input = input().strip().lower()
    if user_input in ["y", "yes"]:
        write_report(report)
    else:
        print("No report saved, exiting...")
    
main()