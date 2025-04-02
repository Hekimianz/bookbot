def count_words(book):
    words = book.split()
    return len(words)
   
def count_chars(book):
    words = book.split()
    chars = {}
    for word in words:
        for char in word: 
            if char.lower() in chars:
                chars[char.lower()] += 1
            else: 
                chars[char.lower()] = 1
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
