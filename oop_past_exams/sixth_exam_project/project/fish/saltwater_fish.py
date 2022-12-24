from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):

    def __init__(self, name, species, price, size=5):
        super().__init__(name, species, size, price)
        # self.size = 5


    def eat(self):
        self.size += 2

