from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTest(TestCase):

    def test_plantation_init_size_correct(self):
        test_plant = Plantation(5)

        self.assertEqual(5, test_plant.size)

    def test_plantation_init_size_wrong(self):
        with self.assertRaises(ValueError) as ex:
            test_plant = Plantation(-5)

        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_plantation_init_plants(self):
        test_plant = Plantation(5)
        self.assertEqual({}, test_plant.plants)

    def test_plantation_init_workers(self):
        test_plant = Plantation(5)
        self.assertEqual([], test_plant.workers)

    def test_plantation_hire_worker_happycase(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")

        self.assertEqual("Petar", test_plant.workers[0])

    def test_plantation_hire_worker_happycase_2(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")
        test_plant.hire_worker("Gosho")

        self.assertEqual(["Petar", "Gosho"], test_plant.workers)

    def test_plantation_hire_worker_happycase_return(self):
        test_plant = Plantation(5)

        self.assertEqual("Petar successfully hired.", test_plant.hire_worker("Petar"))

    def test_plantation_hire_worker_worker_already_hired(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")

        with self.assertRaises(ValueError) as ex:
            test_plant.hire_worker("Petar")

        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_plantation_planting_worker_not_hired(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")

        with self.assertRaises(ValueError) as ex:
            test_plant.planting("Gosho", "daffodil on a pretty string")

        self.assertEqual("Worker with name Gosho is not hired!", str(ex.exception))

    def test_plantation_len_dunder(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")
        test_plant.planting("Petar", "daffodil on a pretty string")
        test_plant.planting("Petar", "rose")

        self.assertEqual(2, len(test_plant))


    def test_plantation_planting_capacity_overdone(self):
        test_plant = Plantation(2)
        test_plant.hire_worker("Petar")
        test_plant.planting("Petar", "daffodil on a pretty string")
        test_plant.planting("Petar", "rose")

        with self.assertRaises(ValueError) as ex:
            test_plant.planting("Petar", "tullip")

        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_plantation_planting_happy_case(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")
        test_plant.planting("Petar", "daffodil on a pretty string")

        self.assertEqual("daffodil on a pretty string", test_plant.plants["Petar"][0])

    def test_plantation_planting_happy_case_2(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")
        test_plant.planting("Petar", "daffodil on a pretty string")
        test_plant.planting("Petar", "rose")

        self.assertEqual(["daffodil on a pretty string", "rose"], test_plant.plants["Petar"])

    def test_plantation_planting_happy_case_3(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")
        test_plant.planting("Petar", "daffodil on a pretty string")
        test_plant.planting("Petar", "rose")

        test_plant.hire_worker("Gosho")
        test_plant.planting("Gosho", "tulip")

        self.assertEqual(["tulip"], test_plant.plants["Gosho"])

    def test_plantation_planting_happy_case_first_plant_return(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")

        self.assertEqual("Petar planted it's first rose.", test_plant.planting("Petar", "rose"))

    def test_plantation_planting_happy_case_second_plant(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")
        test_plant.planting("Petar", "rose")

        self.assertEqual("Petar planted tulip.", test_plant.planting("Petar", "tulip"))

    def test_plantation_string_representation_dunder(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")
        test_plant.planting("Petar", "daffodil on a pretty string")
        test_plant.planting("Petar", "rose")

        test_plant.hire_worker("Gosho")
        test_plant.planting("Gosho", "tulip")

        correct = "Plantation size: 5\n"
        correct += "Petar, Gosho\n"
        correct += "Petar planted: daffodil on a pretty string, rose\n"
        correct += "Gosho planted: tulip"

        #Plantation size: 5
        # Petar, Gosho
        # Petar planted: daffodil on a pretty string, rose
        # Gosho planted: tulip

        self.assertEqual(correct, test_plant.__str__())

    def test_plantation_string_representation_dunder(self):
        test_plant = Plantation(5)


        correct = "Plantation size: 5\n"
        # correct += "\n"
        # correct += "\n"

        self.assertEqual(correct, test_plant.__str__())

    def test_plantation_repr_dunder(self):
        test_plant = Plantation(5)
        test_plant.hire_worker("Petar")
        test_plant.planting("Petar", "daffodil on a pretty string")
        test_plant.planting("Petar", "rose")
        test_plant.hire_worker("Gosho")


        correct = "Size: 5\n"
        correct += "Workers: Petar, Gosho"

        self.assertEqual(correct, test_plant.__repr__())


if __name__ == "__main__":
    main()

