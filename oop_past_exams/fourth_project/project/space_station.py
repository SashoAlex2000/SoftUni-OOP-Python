from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist

from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository

from collections import deque


class SpaceStation():
    successful_missions = 0
    unsuccessful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type, name):

        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."

        new_astronaut = eval(astronaut_type)(name)
        self.astronaut_repository.astronauts.append(new_astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):

        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f"{name} is already added."

        new_planet = Planet(name)
        item_list = items.split(", ")
        for item in item_list:
            new_planet.items.append(item)

        self.planet_repository.planets.append(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                self.astronaut_repository.astronauts.remmove(astronaut)
                return f"Astronaut {name} doesn't exist!"

        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):

        planet_exists = False

        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                current_planet = planet
                planet_exists = True

        if not planet_exists:
            raise Exception("Invalid planet name!")

        current_astronauts = []
        sorted_astronauts = (self.astronaut_repository.astronauts).copy()
        sorted_astronauts.sort(key=lambda x: x.oxygen, reverse=True)
        i = 0

        for astronaut in sorted_astronauts:
            if astronaut.oxygen > 30:
                current_astronauts.append(astronaut)
                i += 1
            if i >= 5:
                break

        if len(current_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        mission_is_successful = False
        total_items = len(current_planet.items)
        total_participants = 0

        for astronaut in current_astronauts:
            total_participants += 1
            # for item in reversed(current_planet.items):
            #     astronaut.backpack.append(item)
            #     astronaut.breathe()
            #
            #     if current_planet.items.index(item) == total_items - 1:
            #         mission_is_successful = True
            #         break
            #
            #     if astronaut.oxygen <= 0:
            #         break

            while True:
                item = current_planet.items[-1]
                astronaut.backpack.append(item)
                astronaut.breathe()
                current_planet.items.pop()

                # print(f"{item} - breathing")

                if len(current_planet.items) == 0:
                    mission_is_successful = True
                    break

                if astronaut.oxygen <= 0:
                    break

            if mission_is_successful:
                break

        if mission_is_successful:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {total_participants} astronauts participated in collecting items."

        else:
            self.unsuccessful_missions += 1
            return f"Mission is not completed."

    def report(self):
        result = ""
        result += f"{self.successful_missions} successful missions!\n"
        result += f"{self.unsuccessful_missions} missions were not completed!\n"
        result += "Astronauts' info:\n"

        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n"
            result += f"Oxygen: {astronaut.oxygen}\n"
            if len(astronaut.backpack) > 0:
                result += f"Backpack items: {', '.join(astronaut.backpack)}\n"
            else:
                result += f"Backpack items: none\n"

        return result


# test_space_station = SpaceStation()
#
# print(test_space_station.add_astronaut("Biologist", "Sasho"))
# print(test_space_station.add_astronaut("Geodesist", "Gosho"))
# print(test_space_station.add_astronaut("Geodesist", "Petko"))
# print(test_space_station.add_astronaut("Meteorologist", "Stanko"))
#
# print(test_space_station.add_planet("Mars", "clay, rocks, alien tech, MARS Rover, banica, Tesla, banana"))
#
# for astronaut in test_space_station.astronaut_repository.astronauts:
#     print(astronaut.oxygen)
#
# for planet in test_space_station.planet_repository.planets:
#     print(planet.items)
#
# print(test_space_station.send_on_mission("Mars"))
# print(test_space_station.successful_missions)
# print(test_space_station.unsuccessful_missions)
#
# for astronaut in test_space_station.astronaut_repository.astronauts:
#     print(f"{astronaut.name} {astronaut.backpack}")
#
# for astronaut in test_space_station.astronaut_repository.astronauts:
#     print(f"{astronaut.name} {astronaut.oxygen}")
#
# for planet in test_space_station.planet_repository.planets:
#     print(planet.items)
#
# print(test_space_station.report())
# test_space_station.recharge_oxygen()
# print(test_space_station.report())
