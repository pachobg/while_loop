needed_book = input()

book_count = 0

book = input()
while book != needed_book:
    if book == "No More Books":
        break
    book_count += 1
    book = input()
if book == needed_book:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
