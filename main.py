from stats import get_word_count
from stats import get_all_characters
from stats import sort_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
   
def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    word_count = get_word_count(book_text)
    #print(f"{word_count} words found in the document")
    
    amount = get_all_characters(book_text)
    sort_char(amount)
    
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = get_word_count(book_text)
    
    amount = get_all_characters(book_text)
    sorted_chars = sort_char(amount)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print only alphabetical characters
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
