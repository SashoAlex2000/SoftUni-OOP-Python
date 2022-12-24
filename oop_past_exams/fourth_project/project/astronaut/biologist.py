from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    def __init__(self, name, oxygen=70):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 5



# test_bnio = Biologist("ELI")
# print(test_bnio.oxygen)
# print(test_bnio.backpack)
# test_bnio.breathe()
# print(test_bnio.oxygen)
