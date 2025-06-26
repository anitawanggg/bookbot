import sys
from stats import word_count, character_count, sorted_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    text = get_book_text(bookpath)
    num_words = word_count(text)
    list_dict = sorted_dict(character_count(text))

    print(f"""
============ BOOKBOT ============
Analyzing book found at {bookpath}
----------- Word Count ----------
Found {num_words} total words 
--------- Character Count -------
""")

    for item in list_dict:
        if not item["char"].isalpha():
            continue
        print(f'{item["char"]}: {item["num"]}')

    return

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()

    return book_text


main()