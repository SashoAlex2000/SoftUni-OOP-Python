from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return ("BRAK!")


class Cat(Animal):
    def make_sound(self):
        return("MEOW!")


class Chicken(Animal):
    def make_sound(self):
        return("q elate pilenca pri batko")



def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
