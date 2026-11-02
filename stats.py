def get_book_text(b):
    with open(b) as f:
        content = f.read()
    return content


def main():
    book_obtained = get_book_text("books/frankenstein.txt")
    return(book_obtained)   
new_words = main()

new_words_split = new_words.split()
print(f"Found {len(new_words_split)} total words.")
