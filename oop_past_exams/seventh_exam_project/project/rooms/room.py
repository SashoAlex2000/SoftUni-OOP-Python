from project.appliances.appliance import Appliance
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge

from project.people.child import Child


class Room():

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0

        for item in args:
            if item.__class__.__name__ == "Child":
                total_cost += (item.cost) * 30
            else:
                total_cost += item.get_monthly_expense()

        return total_cost




# test_room = Room("Staq 402", 250, 3)
# test_appliance1 = TV()
# test_appliance2 = Stove()
# test_appliance3 = Fridge()
#
# print(test_room.calculate_expenses(test_appliance1, test_appliance2, test_appliance3))
