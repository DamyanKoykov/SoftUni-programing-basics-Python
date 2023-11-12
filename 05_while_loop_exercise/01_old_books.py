book_to_find = input()

book_checked_counter = 0
book_found = False
no_more_books = False

while not book_found and not no_more_books:
    checked_book = input()
    if book_to_find == checked_book:
        book_found = True
        break
    if checked_book == "No More Books":
        no_more_books = True
        break
    book_checked_counter += 1

if book_found:
    print(f"You checked {book_checked_counter} books and found it.")
elif no_more_books:
    print(f"The book you search is not here! \nYou checked {book_checked_counter} books.")
