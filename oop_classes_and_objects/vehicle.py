class Vehicle:
    def __init__(self, mileage, max_speed=None):
        self.mileage = mileage
        self.max_speed = max_speed if max_speed else 150
        self.gadgets = []

    def test_print(self
                   ):
        return f"mileage:{self.mileage}; max_speed:{self.max_speed}"


car1 = Vehicle(100000)
car2 = Vehicle(100000, 200)

print(car1.test_print())
print(car2.test_print())

car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
