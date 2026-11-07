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

def counting_characters(c):
    count_character = {}
    for character in c:
        if character.lower() in count_character:
            count_character[character.lower()] += 1
        else:
            count_character[character.lower()] = 1
    return count_character

def sort_on(count_character: tuple[str, int]) -> int:
    return count_character[1]
    
def chars_dict_to_sorted_list(count_character: dict[str, int]) -> list[tuple[str, int]]:
    chars_sorted = []
    for counting_character in count_character:
        chars_sorted.append((counting_character, count_character[counting_character]))
    return sorted(chars_sorted, key=sort_on, reverse=True)


    
