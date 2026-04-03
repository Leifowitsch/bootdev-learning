from stats import counting_words
from stats import printing_dict
from stats import get_book_text
from stats import making_dict_sortready
from stats import counting_characters

import sys

def main():
    if len(sys.argv) < 2:
        print("\n\nUsage: python3 main.py <path_to_book>\n\n")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        words = counting_words(get_book_text(file_path))
        print("\n\nUsage: python3 main.py <path_to_book>\n\n")
        print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        printing_dict(making_dict_sortready(counting_characters(get_book_text(file_path))))
        print("============= END ===============")
    
main()
