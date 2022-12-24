from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name, capacity):

        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        stripped_value = "".join([ch for ch in value if ch != " "])
        if len(stripped_value) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        total_sum = 0

        if len(self.fish) == 0:
            return 0
        for decoration in self.decorations:
            total_sum += decoration.comfort

            return total_sum

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = ""
        result += f"{self.name}:\n"
        if len(self.fish) > 0:
            result += f"Fish: " + " ".join([fish.name for fish in self.fish]) + "\n"
        else:
            result += f"Fish: none\n"

        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"

        return result

