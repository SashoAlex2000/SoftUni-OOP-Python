from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop

from project.people.child import Child
from project.rooms.room import Room
from project.rooms.young_couple_with_children import YoungCoupleWithChildren
from project.rooms.old_couple import OldCouple
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung


class Everland():

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_cost = 0

        for room in self.rooms:
            total_cost += room.expenses
            total_cost += room.room_cost
            # total_cost += (room.room_cost * 30)

        return f"Monthly consumption: {total_cost:.2f}$."

    def pay(self):
        result = ""

        for room in self.rooms:
            # room_cost = room.expenses + (room.room_cost * 30)
            room_cost = room.expenses + room.room_cost

            if self.rooms.index(room) < len(self.rooms) - 1:
                if room_cost <= room.budget:
                    room.budget -= room_cost
                    result += f"{room.family_name} paid {room_cost:.2f}$ and have {room.budget:.2f}$ left.\n"
                else:
                    result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                    self.rooms.remove(room)

            else:
                if room_cost <= room.budget:
                    room.budget -= room_cost
                    result += f"{room.family_name} paid {room_cost:.2f}$ and have {room.budget:.2f}$ left."
                else:
                    result += f"{room.family_name} does not have enough budget and must leave the hotel."
                    self.rooms.remove(room)

        return result

    def status(self):
        result = ""
        total_population = 0
        for room in self.rooms:
            total_population += room.members_count

            total_population += len(room.children)

        result += f"Total population: {total_population}\n"

        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count + len(room.children)} members. Budget: {room.budget:.2f}$, " \
                      f"Expenses: {room.expenses:.2f}$\n"

            if len(room.children) > 0:
                for child in room.children:
                    result += f"--- Child {room.children.index(child) + 1} monthly cost: {(child.cost * 30):.2f}$\n"

            result += f"--- Appliances monthly cost: {sum((app.cost * 30) for app in room.appliances):.2f}$\n"

        return result



# test_everland = Everland()
#
# test_child = Child(10, 15, 2)
#
# test_young_copule_kids = YoungCoupleWithChildren("Malinovi", 3000, 5000, test_child)
# print(test_young_copule_kids.expenses)
#
# test_everland.add_room(test_young_copule_kids)
#
# test_old_couple_room = OldCouple("Petrovi", 250, 300)
# # print(test_old_couple_room.budget)
# print(test_old_couple_room.expenses)
# test_everland.add_room(test_old_couple_room)
#
# print(test_everland.get_monthly_consumptions())
#
# for room in test_everland.rooms:
#     print(f"{room.family_name} {room.expenses + (room.room_cost * 30)}")
# #
# # print(test_everland.pay())
# #
# # print(test_everland.pay())
#
# print(test_everland.status())
