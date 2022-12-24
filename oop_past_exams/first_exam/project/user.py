#DA TI EBA MAIKATA

class User():

    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []


    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        value_list = list(value)
        test_value = "".join(ch for ch in value_list if ch != " ")
        if test_value == " " or test_value == "":
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        result = ""
        result += f"Username: {self.username}, Age: {self.age}\n"
        result += "Liked movies:\n"
        if len(self.movies_liked) <= 0:
            result += "No movies liked.\n"
        else:
            for movie in self.movies_liked:
                result += f"{movie.details()}\n"

        result += "Owned movies:\n"

        if len(self.movies_owned) <= 0:
            result += "No movies owned."
        else:
            for movie in self.movies_owned:
                if self.movies_owned.index(movie) < len(self.movies_owned) - 1:
                    result += f"{movie.details()}\n"
                else:
                    result += f"{movie.details()}"

        return result


#
# test_user = User("Sasho", 22)
# # print(test_user.username)
# # test_user2 = User("", 22)
# # test_user = User("Sasho", 1)
# # test_thriller = thriller.Thriller("Django", 2013, test_user)
# print(test_user)