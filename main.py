def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
def word_counter(book):
    num_words = book.split()
    return len(num_words)

def main ():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    print(book_text)
    print (f"{word_counter(book_text)} words found in the document.")

main()