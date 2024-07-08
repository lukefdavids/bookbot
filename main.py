def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    create_dict_list(character_count)
    print(f"Your document contains {word_count} total words.")
    print(f"Here is how many times each letter of the alphabet was used in your document:")
    print()

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
    list_of_dicts = []
    
    #remove non-alphabetical characters:
    non_alpha_chars = []
    for c in character_count:
        if c.isalpha() == False:
            non_alpha_chars.append(c)

    for c in non_alpha_chars:
        del character_count[c]
    
    #convert the "chars" dictionary into a list of dictionaries:
    for key, value in character_count.items():
        list_of_dicts.append({key: value})
    print(list_of_dicts)


main()