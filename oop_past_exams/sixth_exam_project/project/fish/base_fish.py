from abc import ABC, abstractmethod


class BaseFish(ABC):

    def __init__(self, name, species, size, price):

        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__species

    @name.setter
    def name(self, value):

        test_value = "".join([ch for ch in value if ch != " "])

        if len(test_value) == 0:
            raise ValueError("Fish name cannot be an empty string.")

        self.__species = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):

        test_value = "".join([ch for ch in value if ch != " "])

        if len(test_value) == 0:
            raise ValueError("Fish species cannot be an empty string.")

        self.__species = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):

        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")

        self.__price = value

    @abstractmethod
    def eat(self):
        self.size += 5


