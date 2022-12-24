from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            pass
        else:
            current_horse = eval(horse_type)(horse_name, horse_speed)

            for horse in self.horses:
                if horse.name == horse_name:
                    raise Exception(f"Horse {horse_name} has been already added!")

            self.horses.append(current_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        new_jockey = Jockey(jockey_name, age)

        for existing_j in self.jockeys:
            if existing_j.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):

        new_horse_race = HorseRace(race_type)

        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        # new_horse_race = HorseRace(race_type)

        self.horse_races.append(new_horse_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey_exists = False
        current_jockey = None

        for jock in self.jockeys:
            if jock.name == jockey_name:
                jockey_exists = True
                current_jockey = jock
                break

        if not jockey_exists:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        current_horse = None

        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type:
                if not horse.is_taken:
                    current_horse = horse
                    break

        if current_horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        else:
            if current_jockey.horse is not None:
                return f"Jockey {current_jockey.name} already has a horse."

            else:
                current_jockey.horse = current_horse
                # current_horse.jockey = current_jockey
                current_horse.is_taken = True

                return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        race_exists = False
        current_race = None

        for race in self.horse_races:
            if race.race_type == race_type:
                race_exists = True
                current_race = race

        if not race_exists:
            raise Exception(f"Race {race_type} could not be found!")

        current_jockey = None
        jockey_exists = False

        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                current_jockey = jockey
                jockey_exists = True

        if not jockey_exists:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if current_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if current_jockey in current_race.jockeys:
            return f"Jockey {current_jockey.name} has been already added to the {race_type} race."

        current_race.jockeys.append(current_jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        race_exists = False
        current_race = None

        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                race_exists = True
                current_race = horse_race

        if not race_exists:
            raise Exception(f"Race {race_type} could not be found!")

        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        max_speed = 0

        for jockey in current_race.jockeys:
            if jockey.horse.speed > max_speed:
                max_speed = jockey.horse.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."



#
# test_horse_app = HorseRaceApp()
# print(test_horse_app.add_horse("Appaloosa", "Gosho", 100))
# print(test_horse_app.add_horse("Appaloosa", "Sasaa", 100))
# print(test_horse_app.add_horse("Appaloosa", "Cunci", 105))
# print(test_horse_app.add_jockey("Alex", 22))
# print(test_horse_app.add_jockey("Vutev", 22))
# print(test_horse_app.add_jockey("Koko", 22))
# # print(test_horse_app.add_jockey("Alex", 111))
#
# print(test_horse_app.create_horse_race("Winter"))
# print(test_horse_app.create_horse_race("Summer"))
# # print(test_horse_app.create_horse_race("Summer"))
#
#
# print(test_horse_app.add_horse_to_jockey("Alex", "Appaloosa"))
# print(test_horse_app.add_horse_to_jockey("Vutev", "Appaloosa"))
# print(test_horse_app.add_horse_to_jockey("Vutev", "Appaloosa"))
# # print(test_horse_app.add_horse_to_jockey("Koko","Thoroughbred"))
#
# # for jock in test_horse_app.jockeys:
# #     print(jock.horse.name)
#
# print(test_horse_app.add_jockey_to_horse_race("Winter", "Alex"))
# print(test_horse_app.add_jockey_to_horse_race("Winter", "Vutev"))
#
# for race in test_horse_app.horse_races:
#     for jockey in race.jockeys:
#         print(jockey.name)
#         print(jockey.horse.name)
#
# print(test_horse_app.start_horse_race("Winter"))
#
# test_horse = Appaloosa("Konche", 100)
# test_horse.train()
# test_horse.train()
# test_horse.train()
# print(test_horse.speed)
# test_horse.train()
# test_horse.train()
# test_horse.train()
# test_horse.train()
# test_horse.train()
# test_horse.train()
# test_horse.train()
# test_horse.train()
# print(test_horse.speed)
# test_horse.train()
# test_horse.train()
# test_horse.train()
# print(test_horse.speed)

