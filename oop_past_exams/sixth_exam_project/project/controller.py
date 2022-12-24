from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium

from project.decoration.base_decoration import BaseDecoration
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.decoration.decoration_repository import DecorationRepository


class Controller():

    def __init__(self):
        self.decoration_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."

        new_aquarium = eval(aquarium_type)(aquarium_name)
        self.aquariums.append(new_aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):

        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."

        new_decoration = eval(decoration_type)()

        self.decoration_repository.add(new_decoration)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        aquarium_exists = False
        current_aquarium = None

        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                current_aquarium = aquarium
                aquarium_exists = True
                break

        if not aquarium_exists:
            pass
        else:
            for decoration in self.decoration_repository.decorations:
                if decoration.__class__.__name__ == decoration_type:
                    current_aquarium.decorations.append(decoration)
                    self.decoration_repository.decorations.remove(decoration)
                    return f"Successfully added {decoration_type} to {aquarium_name}."

            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        if fish_type == "FreshwaterFish":
            searched_tank = "FreshwaterAquarium"
        else:
            searched_tank = "SaltwaterAquarium"

        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                if searched_tank != aquarium.__class__.__name__:
                    return "Water not suitable."

                current_fish = eval(fish_type)(fish_name, fish_species, price)
                return aquarium.add_fish(current_fish)

    def feed_fish(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                for fish in aquarium.fish:
                    fish.eat()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                total_value = 0
                for fish in aquarium.fish:
                    total_value += fish.price

                for decoration in self.decoration_repository.decorations:
                    total_value += decoration.price

                return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        result = ""

        for aquarium in self.aquariums:
            result += f"{aquarium.name}:\n"
            if len(aquarium.fish) > 0:
                result += f"Fish: " + " ".join([fish.name for fish in aquarium.fish]) + "\n"
            else:
                result += f"Fish: none\n"

            result += f"Decorations: {len(aquarium.decorations)}\n"
            result += f"Comfort: {aquarium.calculate_comfort()}\n"

        return result



# test_controller = Controller()
#
# print(test_controller.add_aquarium("FreshwaterAquarium", "AQUA Base"))
# print(test_controller.add_aquarium("SaltwaterAquarium", "Salty chad"))
#
# for aquarium in test_controller.aquariums:
#     print(f"{aquarium.__class__.__name__} - {aquarium.name}")
#
# print(test_controller.add_decoration("Plant"))
# print(test_controller.add_decoration("Plant"))
# print(test_controller.add_decoration("Ornament"))
#
# for decoration in test_controller.decoration_repository.decorations:
#     print(f"{decoration.__class__.__name__} - {decoration.price} {decoration.comfort}")
#
# print(test_controller.insert_decoration("AQUA Base", "Plant"))
# print(test_controller.insert_decoration("AQUA Base", "Ornament"))
#
# for aquarium in test_controller.aquariums:
#     print(", ".join(decoration.__class__.__name__ for decoration in aquarium.decorations))
#
# print(test_controller.add_fish("AQUA Base", "FreshwaterFish", "Sasho", "Salmon", 69))
# print(test_controller.add_fish("Salty chad", "FreshwaterFish", "Sasho", "Salmon", 69))
#
# for aquarium in test_controller.aquariums:
#     print(f"{aquarium.name} - {aquarium.fish}")
#
# print(test_controller.feed_fish("AQUA Base"))
# print(test_controller.calculate_value("AQUA Base"))
#
# # for aquarium in test_controller.aquariums:
# #     print(aquarium)
#
# print(test_controller.report())