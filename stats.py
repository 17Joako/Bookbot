def word_counter(book):
    num_words = book.split()
    return len(num_words)
def char_counter(book):
    book = book.lower()
    num_chars = {}
    for char in book:
        num_chars[char] = num_chars.get(char, 0) + 1
    return num_chars