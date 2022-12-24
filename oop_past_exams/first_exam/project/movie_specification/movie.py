from abc import abstractmethod, ABC
from project.user import User

class Movie(ABC):

    def __init__(self, title, year, owner):
        self.title = title
        self.year = year
        self.owner = owner
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        value_list = list(value)
        test_value = "".join(ch for ch in value_list if ch != " ")
        if test_value == " " or test_value == "":
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")

        self.__owner = value

    @abstractmethod
    def details(self):
        pass
