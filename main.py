def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = count_characters(text)

    # Create the list of dictionaries
    char_list = []
    for char, count in characters.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    
    # Sort the list
    char_list.sort(reverse=True, key=sort_on)

    # Print the report    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    # Loop through the sorted list to print each character's count
    for item in char_list:
        print(f" The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_characters(text):
    characters_dict = {} 
    for char in text:
        char = char.lower()
        if char.isalpha() == True:
            if char in characters_dict:
                characters_dict[char] += 1
            else:
                characters_dict[char] = 1
    return characters_dict   

def sort_on(dict):
    return dict["num"]

main()