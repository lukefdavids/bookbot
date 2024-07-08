def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    cleaned_character_count = create_dict_list(character_count)
    character_list = sort(cleaned_character_count)
    
    print("------------------------------------------")
    print(f"Begin report of {book_path}")
    print("")
    print(f"Total words: {word_count}")
    print("")
    for key, value in character_list:
        print(f"The letter '{key}' appeared {value} times")
    print("")
    print("End report")
    print("------------------------------------------")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(frankenstein):
    words = frankenstein.split()
    return len(words)  

def count_characters(frankenstein):
    chars = {}
    for c in frankenstein:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def create_dict_list(character_count):
    non_alpha_chars = [c for c in character_count if not c.isalpha()]
    for c in non_alpha_chars:
        del character_count[c]
    
    return character_count

def sort(character_count):
    sorted_items = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_items

main()