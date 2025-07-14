import sys
from stats import generate_char_report, get_number_of_words, get_char_count, get_book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    content = get_book_text(book_path)
    word_count = get_number_of_words(content)
    char_count = get_char_count(content)
    report = generate_char_report(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in report:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
