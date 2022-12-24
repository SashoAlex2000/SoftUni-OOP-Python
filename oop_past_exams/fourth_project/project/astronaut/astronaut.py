from abc import ABC, abstractmethod

class Astronaut(ABC):

    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        stripped_value = "".join([ch for ch in value if ch != " "])

        if len(stripped_value) == 0:
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount



