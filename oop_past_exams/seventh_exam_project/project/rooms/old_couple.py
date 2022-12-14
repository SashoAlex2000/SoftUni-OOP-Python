from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple (Room):

    def __init__(self, family_name, pension_one, pension_two):

        super().__init__(family_name, (pension_one + pension_two), 2)
        self.room_cost = 15
        self.appliances = [TV(), Stove(), Fridge(), TV(), Stove(), Fridge()]
        self.expenses = self.calculate_expenses(*(self.appliances))


# test_old_couple_room = OldCouple("Petrovi", 250, 300)
# print(test_old_couple_room.budget)
# print(test_old_couple_room.expenses)