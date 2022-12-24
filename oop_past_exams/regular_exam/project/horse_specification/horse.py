from abc import ABC, abstractmethod


class Horse(ABC):

    MAXIMUM_SPEED = 10000
    SPEED_GAINED_TRAINING = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):

        if value > self.MAXIMUM_SPEED:
            raise ValueError("Horse speed is too high!")

        self.__speed = value

    @abstractmethod
    def train(self):
        # if self.speed + self.SPEED_GAINED_TRAINING > self.MAXIMUM_SPEED:
        #     self.speed = self.MAXIMUM_SPEED
        # else:
        #     self.speed += self.SPEED_GAINED_TRAINING
        pass
