

class User:
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        sorted_books = sorted(self.books)
        result = " ".join(sorted_books)
        return result

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

# test_user = User("6969","ALEX")
# print(test_user)
