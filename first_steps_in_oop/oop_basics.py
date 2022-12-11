nums_1 = [1, 2, 3]  # < -- nums1 is and object, an instance of the class 'list' in Python
nums2 = [4, 5, 6]


class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


author1 = Author("Walter", "Isakson")
author2 = Author("Paul","Hetcher")



class Book:
    def __init__(self, title, author, publisher, image_url, price, short_desc):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.image_url = image_url
        self.price = price
        self.short_desc = short_desc

    def open(self):
        print(f"open the books: {self.title} with author {self.author.first_name} {self.author.last_name}")

book1 = Book("S. Jobs - Autobiography", author1, "SoftPress", "aa.png", 35, "...")
book2 = Book("Java for Beginners", author2, "UNWE", "bb.png", 24, "Lear JScript")
book3 = Book("Java for Beginners", author2, "UNWE", "bb.png", 24, "Lear JScript")  # < --- пак е различна
# инстанция

print(book2.title)
print(book1.title)
print(type(book1))
print(id(book1))
print(id(book2))
print(id(book3))

basket = []

basket.append(book1)
basket.append(book2)

total_price = 0

for book in basket:
    total_price += book.price

print(total_price)

print(book1.author.first_name)

print(book1.open())
print("!!!")
book1.open()
book2.open()