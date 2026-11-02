def get_book_text(b):
    with open(b) as f:
        content = f.read()
    return content


def main():
    book_obtained = get_book_text("books/frankenstein.txt")
    print(book_obtained) 
main()    