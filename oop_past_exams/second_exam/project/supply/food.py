from project.supply.supply import Supply


class Food(Supply):

    def __init__(self, name, energy=25):
        super().__init__(name, energy)
        self.energy = energy

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"


#
# test_food = Food("cici")
# print(test_food.details())