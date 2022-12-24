# from project.controller import Controller
# from project.player import Player
# from project.supply.drink import Drink
# from project.supply.food import Food
#
#
#
#
# test_controller = Controller()
# test_player = Player("Sasho", 22, 99)
# print(test_player.name)
# print(Player.already_used_names)
# test_player2 = Player("Gosho", 12, 13)
# print(test_controller.add_player(test_player, test_player2))
#
# test_supply1 = Food("banica", 40)
# test_supply2 = Food("dunerche", 50)
# print(test_controller.add_supply(test_supply1, test_supply2))
# print(test_controller.sustain("Sasho", "Food"))
# print(test_controller.sustain("Gosho", "Food"))
#
# print(test_player2.stamina)
# print(test_player.stamina)
#
# print(test_controller.duel("Sasho", "Gosho"))
# print(test_player2.stamina)
# print(test_player.stamina)

from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food

controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# for supply in controller.supplies:
#     print(supply.name)
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
print(controller.sustain("Lilly", "Drink"))
print(controller.sustain("Lilly", "Drink"))

# for supply in controller.supplies:
#     print(supply.name)

# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
# print(controller)
