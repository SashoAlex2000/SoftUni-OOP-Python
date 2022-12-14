# AMMM

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} {self.author}"


class Library():

    def __init__(self):
        self.books = []

    def find_book(self, title):
        try:
            for book in self.books:
                if book.title == title:
                    return book
        except IndexError:
            return "Book not found"
        else:
            return "No such book"

    def add_book(self, book):
        self.books.append(book)

library = Library()



for num in range(1,11):
    book = Book(f"Title {num}", f"Author {num**2}")
    library.books.append(book)

print(library.find_book("Title 156"))