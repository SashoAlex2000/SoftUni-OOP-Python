class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)


from unittest import TestCase, main


class CarTest(TestCase):
    def test_correct_initialization_fuel(self):
        car = Car("Kia", "Sportage", 13, 100)

        self.assertEqual(0, car.fuel_amount)

    def test_correct_initialization_make(self):
        car = Car("Kia", "Sportage", 13, 100)

        self.assertEqual("Kia", car.make)

    def test_correct_initialization_model(self):
        car = Car("Kia", "Sportage", 13, 100)

        self.assertEqual("Sportage", car.model)

    def test_correct_initialization_consumption(self):
        car = Car("Kia", "Sportage", 13, 100)

        self.assertEqual(13, car.fuel_consumption)

    def test_correct_initialization_capacity(self):
        car = Car("Kia", "Sportage", 13, 100)

        self.assertEqual(100, car.fuel_capacity)

    def test_wrong_make(self):
        car = Car("Kia", "Sportage", 13, 100)

        with self.assertRaises(Exception) as ex:
            car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_wrong_model(self):
        car = Car("Kia", "Sportage", 13, 100)

        with self.assertRaises(Exception) as ex:
            car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    # Fuel consumption cannot be zero or negative!

    def test_negative_fuel_consumption(self):
        car = Car("Kia", "Sportage", 13, 100)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -10

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_zero_fuel_consumption(self):
        car = Car("Kia", "Sportage", 13, 100)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    # Fuel capacity cannot be zero or negative!

    def test_negative_fuel_capacity(self):
        car = Car("Kia", "Sportage", 13, 100)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -10

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_zero_fuel_capacity(self):
        car = Car("Kia", "Sportage", 13, 100)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    # Fuel amount cannot be negative!

    def test_negative_fuel(self):
        car = Car("Kia", "Sportage", 13, 100)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -100

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_changed_correctly(self):
        car = Car("Kia", "Sportage", 13, 100)

        car.fuel_amount = 45

        self.assertEqual(45, car.fuel_amount)

    # Fuel amount cannot be zero or negative!
    def test_refuel_negative_amount(self):
        car = Car("Kia", "Sportage", 13, 100)

        with self.assertRaises(Exception) as ex:
            car.refuel(-15)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_zero_amount(self):
        car = Car("Kia", "Sportage", 13, 100)

        with self.assertRaises(Exception) as ex:
            car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_correct_refuel_below_cap(self):
        car = Car("Kia", "Sportage", 13, 100)
        car.refuel(50)
        self.assertEqual(50, car.fuel_amount)

    def test_correct_refuel_above_cap(self):
        car = Car("Kia", "Sportage", 13, 100)
        car.refuel(150)
        self.assertEqual(100, car.fuel_amount)

    # You don't have enough fuel to drive!
    def test_drive_not_enough_fuel(self):
        car = Car("Kia", "Sportage", 13, 100)
        car.refuel(25)

        with self.assertRaises(Exception) as ex:
            car.drive(300)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_happy_case(self):
        car = Car("Kia", "Sportage", 13, 100)
        car.refuel(30)

        car.drive(200)

        self.assertEqual(4, car.fuel_amount)


if __name__ == "__main__":
    main()

