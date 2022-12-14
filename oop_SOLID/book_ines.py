

class Book:
    def __init__(self,content, author, title):
        self.title = title
        self.author = author
        self.content = content



class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)


class PrePrintFlair:
    def format(self, book):
        return f"*************\n{book.title}\n*************\n{book.author}\n*************\n"


normal_formater = Formatter()
flair_formatter = PrePrintFlair()
book1 = Book("Content, 550 pages", "Ivo", "Siromaha")
content_printer = Printer(normal_formater)
print(content_printer.get_book(book1))
flair_printer = Printer(flair_formatter)
print(flair_printer.get_book(book1))