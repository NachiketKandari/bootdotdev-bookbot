from stats import *
import sys

def main():
    print("============ BOOKBOT ============")
    print("Usage: python3 main.py <path_to_book>")

    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}...")
    book_text = get_book_text(file_path)
    
    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    count_dict = count_char(book_text)
    sorted_dict = get_sorted_dict(count_dict)
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")


main()