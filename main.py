import sys
from stats import count_words, count_chars, order_stats, print_stats
def get_book_text(filepath):
    with open(filepath) as book:
        file_contents = book.read()
    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath=sys.argv[1]
    chars = order_stats(count_chars(get_book_text(filepath)))
    words = count_words(get_book_text(filepath))
    print_stats(chars, filepath, words)
    

  

main()