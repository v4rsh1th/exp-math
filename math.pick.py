import random

with open("math_books.txt", "r") as x:
    books = list(x)
    length = len(books)
    randomBook = random.randint(0, len(books))
    print(books[randomBook])