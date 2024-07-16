def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_letters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    list = sort_letters(letters)
    make_repport(list)
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_letters(text):
    letters = {}
    lower_case = text.lower()
    for letter in lower_case:
        if letter in letters:
            number = letters[letter]
            number += 1
            letters.update({letter:number})
        else:
            letters[letter] = 1
    return letters


def sort_on(dict):
    return dict["num"]


def sort_letters(input):
    result = []
    for letter,number in input.items():
        if letter.isalpha() == True:
            result.append({"character":letter, "num":number})
    result.sort(reverse=True, key=sort_on)
    return result


def make_repport(list):
    print("")
    for x in list:
        y,z = x.values()
        print(f"The '{y}' character was found {z} times")
    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()

main()