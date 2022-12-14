
class Shape():
    def calculate_area(self):
        pass


class Triangle(Shape):
    def __init__(self, h, side):
        self.h = h
        self.side = side


    def calculate_area(self):
        print("Calculating triangle area")


class Circle(Shape):
    def __init__(self, r):
        self.r = r


    def calculate_area(self):
        print("Calculating circle area")




shapes = [Triangle(5 ,2), Circle(5)]

for shape in shapes:
    shape.calculate_area()


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __le__(self, other):    # < --- means "<="
        return self.age <= other.age     # < --- wil work only with instances which have age

    def __eq__(self, other):
        if not isinstance(other, Cat):
            raise ValueError(f"Operand not supported between an instance of {self.__class__.__name__} "
                             f"and {other.__class__.__name__}")

        if self.name == other.name and self.age == other.age:
            return True
        return False

class MiniCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)


cat1 = Cat("Misho", 2)
cat2 = Cat("ana", 13)
cat3 = Cat("ana", 13)
mini_cat = MiniCat("malcho", 13)

# print(cat1 < cat2)    # TypeError, "<" not supported between intances
print(cat1 <= cat2)
print(cat1.__le__(cat2))
# print(cat1 <= 5)        # object int doesnt have attribute age
print(cat1 >= cat2)     # returns False, it looks at <=
print(cat1 == cat2)
print(cat3 == cat2)
# print(cat3 == "kuche")
# print(mini_cat == "kuche")
print(mini_cat == cat2)