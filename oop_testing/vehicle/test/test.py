from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTest(TestCase):

    def test_vehicle_init_fuel(self):
        vehicle = Vehicle(100, 300)

        self.assertEqual(100, vehicle.fuel)

    def test_vehicle_init_horese_power(self):
        vehicle = Vehicle(100, 300)

        self.assertEqual(300, vehicle.horse_power)

    def test_vehicle_init_capacity(self):
        vehicle = Vehicle(100, 300)

        self.assertEqual(100, vehicle.capacity)

    def test_vehicle_init_consumption(self):
        vehicle = Vehicle(100, 300)

        self.assertEqual(1.25, vehicle.fuel_consumption)

    def test_vehicle_drive_to_much_km(self):
        vehicle = Vehicle(100, 300)

        with self.assertRaises(Exception) as ex:
            vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle_drive_real(self):
        vehicle = Vehicle(100, 300)
        vehicle.drive(10)

        self.assertEqual(87.5, vehicle.fuel)

    def test_vehicle_refuel_too_much_fuel(self):
        vehicle = Vehicle(100, 300)

        vehicle.drive(50)

        with self.assertRaises(Exception) as ex:
            vehicle.refuel(150)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_right_refuel(self):
        vehicle = Vehicle(100, 300)
        vehicle.drive(10)
        vehicle.refuel(10)

        self.assertEqual(97.5, vehicle.fuel)

    def test_vehicle_string_repr(self):
        vehicle = Vehicle(100, 300)

        correct = f"The vehicle has 300 " \
                  f"horse power with 100 fuel left and 1.25 fuel consumption"

        self.assertEqual(correct, vehicle.__str__())


if __name__ == "__main__":
    main()
