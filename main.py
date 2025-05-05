from stats import count_words
from stats import count_characters

def get_book_text(file_path):
    file_contents = ""

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")

    num_words = count_words(frankenstein)
    num_chars = count_characters(frankenstein)

    print(f"{num_words} words found in the document")

    print(f"{num_chars} characters found in the document")

main()