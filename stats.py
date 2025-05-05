def count_words(book):
    count = 0
    words = book.split()

    for word in words:
        count += 1

    return count

def count_characters(book):
    letter_count = {}

    for i in range(0, len(book)):
        if book[i].lower() not in letter_count:
            letter_count[book[i].lower()] = 1
        else:
            letter_count[book[i].lower()] += 1

    return letter_count