def get_word_count(book_text):
    words = book_text.split()
    num_words = len(words)

    return num_words
 
def get_all_characters(book_text):
    
    amount_of_characters = {}
    
    for character in book_text:
        character = character.lower()

        if character in amount_of_characters:
            amount_of_characters[character] += 1
        else:
            amount_of_characters[character] = 1

    return amount_of_characters

def sort_char(amount_of_characters):
    
    chars_list = []

    for char, count in amount_of_characters.items():
        chars_list.append({"char": char, "count": count})

    def sort_by_count(count):
        return count["count"]
        
    chars_list.sort(reverse=True,key=sort_by_count)
    
    return chars_list
    

