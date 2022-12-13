# START
from project.product import Product


class Food(Product):

    def __init__(self, name):
        super().__init__(name, 15)


# test_food = Food("cherry")
# print(test_food.quantity)
# print(test_food)
