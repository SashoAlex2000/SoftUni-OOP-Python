from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop

from project.people.child import Child


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):

        super().__init__(family_name, (salary_one + salary_two), 2)
        self.room_cost = 30
        self.children = [child for child in children]

        self.appliances = []
        self.expenses = self.calculate_expenses(*self.appliances) + self.calculate_expenses(*self.children)


    @property
    def appliances(self):
        return self.__appliances

    @appliances.setter
    def appliances(self, value):
        value = [TV(), Laptop(), Fridge(), TV(), Laptop(), Fridge()]

        for turn in range(len(self.children)):
            value.append(TV())
            value.append(Laptop())
            value.append(Fridge())

        self.__appliances = value


# test_child = Child(10, 15, 2)
#
# test_young_copule_kids = YoungCoupleWithChildren("Malinovi", 3000, 5000, test_child)
#
# print(test_young_copule_kids.room_cost)
# print(test_young_copule_kids.budget)
# print(test_young_copule_kids.expenses)
# print(len(test_young_copule_kids.appliances))