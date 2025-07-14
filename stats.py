def get_number_of_words(text: str):
    num_words = len(text.split())
    return num_words

def get_char_count(text: str):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def generate_char_report(char_counts: dict[str, int]) -> list[dict[str, int | str]]:
    # Build the list, filtering only alphabetic characters
    report = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]

    # Sort list in-place by 'num', descending
    report.sort(key=lambda item: item["num"], reverse=True)
    return report

def get_book_text(filepath: str) -> str:
    with open(filepath, encoding='utf-8') as f:
        return f.read()