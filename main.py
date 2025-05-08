import sys
from stats import get_num_words, get_num_chars, get_sorted_list

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)

    sorted_list = get_sorted_list(num_chars)
    formatted_list = ""
    for item in sorted_list:
        if item["char"].isalpha():
            formatted_list += f"{item["char"]}: {item["num"]}\n"

    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------\n{formatted_list}")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()