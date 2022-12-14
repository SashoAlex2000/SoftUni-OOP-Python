from project.animals.animal import Mammal
# from project import food as imported_food
from project.food import Food, Meat, Vegetable, Fruit


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        # if not isinstance(food, imported_food.Meat):
        #     return f"{self.name} does not eat {food.__class__.__name__}!"
        if isinstance(food, Fruit) or isinstance(food, Vegetable):
            self.weight += 0.1 * food.quantity
            self.food_eaten += food.quantity

            return

        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity



class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        # if not isinstance(food, imported_food.Meat):
        #     return f"{self.name} does not eat {food.__class__.__name__}!"
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity

            return

        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 1 * food.quantity
        self.food_eaten += food.quantity


# test_cat = Cat("Misho", 16, "kv. Vitosha")
# test_meat = Meat(11)
# print(test_cat.weight)
# test_cat.feed(test_meat)
# print(test_cat.weight)
# test_fruit = Fruit(5)
# print(test_cat.feed(test_fruit))
# print(test_cat)
