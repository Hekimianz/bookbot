def count_words(book):
    words = book.split()
    return len(words)
   
def count_chars(book):
    chars = {}
 
    for char in book:
       lower_char = char.lower()
       if lower_char in chars:
           chars[lower_char] += 1
       else: 
           chars[lower_char] = 1
    return chars



def order_stats(stats):
    toTuple = stats.items()
    return dict(sorted(stats.items(), key=lambda item: item[1], reverse=True))

def print_stats(stats, path, words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for x in stats:
        if x.isalpha():
           print(f"{x}: {stats[x]}")
    print("============= END ===============")
