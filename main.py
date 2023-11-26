def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words(text)
    results = count_alpha_numeric(text)
    count_report(results)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text_block):
    words = text_block.split()
    print(f"Number of words in text is: {len(words)}")


def count_alpha_numeric(text_block):
    words = text_block.split()
    an_count = {}
    for word in words:
        for char in word:
            lower_char = char.lower()
            if lower_char in an_count:
                an_count[lower_char] += 1
            else:
                an_count[lower_char] = 1
    return dict(sorted(an_count.items(), key=lambda x: x[1], reverse=True))


def count_report(alpha_numeric_count: dict):
    for key in alpha_numeric_count:
        count = alpha_numeric_count[key]
        print(f"The '{key}' character was found {count} times")


main()
