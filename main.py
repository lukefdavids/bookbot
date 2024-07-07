def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"Your document contains {word_count} total words.")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(frankenstein):
    words = frankenstein.split() 
    return len(words)  

main()