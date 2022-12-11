from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):

        if book_name in self.books_available[author]:
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username].update({book_name: days_to_return})
            self.books_available[author].remove(book_name)
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            return f'The book "{book_name}" is already rented and will be available in {self.rented_books[user.username][book_name]} days! '

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)

            del self.rented_books[user.username][book_name]

        else:
            return f"{user.username} doesn't have this book in his/her records!"

#
# test_user = User("6969", "ALEX")
# print(test_user)
# library_test = Library()
# library_test.books_available.update({"Ivo siromahov": ["vicove"]})
# library_test.books_available.update({"Michael Connaly": ["Dirty Four"]})
# print(library_test.books_available)
# library_test.get_book("Ivo siromahov", "vicove", 4, test_user)
# library_test.get_book("Michael Connaly", "Dirty Four", 4, test_user)
# print(library_test.get_book("Michael Connaly", "Dirty Four", 4, test_user))
# print(library_test.rented_books)
# print(library_test.books_available)
# print(test_user)
#
# library_test.return_book("Ivo siromahov", "vicove", test_user)
# print(library_test.rented_books)
# print(library_test.books_available)
# print(test_user)
# print(library_test.return_book("Ivo siromahov", "vve", test_user))
