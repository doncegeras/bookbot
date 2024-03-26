def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return(file_contents)


def words_counter(result):
    words = result.split()
    number = 0
    for i in words:
        number +=1
    return(number)

def letter_counter(result):
    lowered_string = result.lower()
    letter_counts ={}
    for char in lowered_string:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char]+=1
            else:
                letter_counts[char] = 1
    return letter_counts

book = main()
words = words_counter(book)
letters = letter_counter(book)

def sort_on(dict):
    return dict[1]


letters_in_words = list(letters.items())

letters_in_words.sort(reverse=True, key=sort_on)


print("--- Begin report of books/frankenstein.txt ---")
print(f"{words} words found in the document")
print()
for letter, count in letters_in_words:
    print(f"The '{letter}' character was found {count} times")
print("--- End report ---")

main()
