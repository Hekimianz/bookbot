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
    text = get_book_text(filepath)
    chars = order_stats(count_chars(text))
    words = count_words(text)
    print_stats(chars, filepath, words)


    

  

main()