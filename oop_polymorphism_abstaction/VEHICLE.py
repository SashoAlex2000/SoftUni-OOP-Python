from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        liters_consumed = distance * (self.fuel_consumption + 0.9)
        if liters_consumed <= self.fuel_quantity:
            self.fuel_quantity -= liters_consumed



class Truck(Vehicle):
    summer_bonus = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def refuel(self, fuel):
        self.fuel_quantity += (0.95 * fuel)

    def drive(self, distance):
        liters_consumed = distance * (self.fuel_consumption + 1.6)
        if liters_consumed <= self.fuel_quantity:
            self.fuel_quantity -= liters_consumed

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

