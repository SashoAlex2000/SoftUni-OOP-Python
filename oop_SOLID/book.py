class Book:
    def __init__(self, content: str, title, author):
        self.content = content
        self.title = title
        self.author = author


class Formatter:
    def format(self, book):
        return book.content


class FlairFormatter:
    def format(self, book):
        return f"*************\n{book.title}\n*************\n{book.author}\n*************\n"


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)


normal_formatter = Formatter()    # <----- we should create an instance of this 

book1 = Book("Content, 550 pages", "Ivo", "Siromaha")
content_printer = Printer(normal_formatter)
print(content_printer.get_book(book1))
#
# flyer_printer = Printer(FlairFormatter)
# print(flyer_printer.get_book(book1))