from stats import new_words
from stats import counting_characters
from stats import new_words_split
characters =  counting_characters(new_words)
print(characters)
from stats import chars_dict_to_sorted_list
sorted_characters = chars_dict_to_sorted_list(characters)
print(sorted_characters)
def print_report(book_name: str, total_words: int, sorted_characters: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for character, count in sorted_characters:
        if character.isalpha():
            print(f"{character}: {count}")
        print(f"{character}: {count}")
print_report("books/frankenstein.txt", len(new_words_split), sorted_characters)