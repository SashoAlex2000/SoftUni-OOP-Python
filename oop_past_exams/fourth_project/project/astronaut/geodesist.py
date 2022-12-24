from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    def __init__(self, name, oxygen=50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 10

#
# test_bnio = Geodesist("ELI")
# print(test_bnio.oxygen)
# print(test_bnio.backpack)
# test_bnio.breathe()
# print(test_bnio.oxygen)
