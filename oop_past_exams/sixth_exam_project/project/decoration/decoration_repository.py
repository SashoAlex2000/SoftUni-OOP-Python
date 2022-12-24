from project.decoration.base_decoration import BaseDecoration
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament


class DecorationRepository():

    def __init__(self):
        self.decorations: list = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):

        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True

        return False

    def find_by_type(self, decoration_type):

        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration

        return "None"

#
# test_repo = DecorationRepository()
#
# test_decoration_1 = Ornament()
# test_decoration_2 = Ornament()
# test_decoration_3 = Ornament()
# test_decoration_4 = Plant()
#
# test_repo.add(test_decoration_1)
# test_repo.add(test_decoration_2)
# test_repo.add(test_decoration_3)
# # test_repo.add(test_decoration_4)
#
# print(test_repo.find_by_type("Plant"))





