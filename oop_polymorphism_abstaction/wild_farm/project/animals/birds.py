from project.animals.animal import Bird
# from project import food as imported_food
from project.food import Food, Meat, Vegetable, Fruit


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):

        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity



# test_owl = Owl("Go6o", 69, 22)
# test_meat = Meat(17)
# print(test_owl.weight)
# test_owl.feed(test_meat)
# print(test_owl.weight)
#
# test_fruit = Fruit(16)
# print(test_owl.feed(test_fruit))
# print(test_owl)

# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)
#
# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)
