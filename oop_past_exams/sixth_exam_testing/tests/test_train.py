from project.train.train import Train
from unittest import TestCase, main


class TrainTest(TestCase):

    def test_init_name_correct(self):
        test_train = Train("Thomas", 25)

        self.assertEqual("Thomas", test_train.name)

    def test_init_capacity_correct(self):
        test_train = Train("Thomas", 25)

        self.assertEqual(25, test_train.capacity)

    def test_init_passengers_correct(self):
        test_train = Train("Thomas", 25)

        self.assertEqual([], test_train.passengers)

    def test_add_function_not_enough_capacity(self):
        test_train = Train("Thomas", 1)
        test_train.add("Gosho")

        with self.assertRaises(ValueError) as ex:
            test_train.add("Alex")

        self.assertEqual("Train is full", str(ex.exception))

    def test_add_function_repeating_name(self):
        test_train = Train("Thomas", 25)
        test_train.add("Gosho")

        with self.assertRaises(ValueError) as ex:
            test_train.add("Gosho")

        self.assertEqual("Passenger Gosho Exists", str(ex.exception))

    def test_add_correct(self):
        test_train = Train("Thomas", 25)
        test_train.add("Gosho")

        self.assertEqual("Gosho", test_train.passengers[0])

    def test_add_correct_second_test(self):
        test_train = Train("Thomas", 25)
        test_train.add("Gosho")
        test_train.add("Alex")

        self.assertEqual(["Gosho", "Alex"], test_train.passengers)

    def test_add_correct_return(self):
        test_train = Train("Thomas", 25)

        self.assertEqual("Added passenger Alex", test_train.add("Alex"))

    def test_remove_passenger_not_in(self):

        test_train = Train("Thomas", 25)
        test_train.add("Gosho")
        test_train.add("Alex")

        with self.assertRaises(ValueError) as ex:
            test_train.remove("Pesho")

        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_correct(self):

        test_train = Train("Thomas", 25)
        test_train.add("Gosho")
        test_train.add("Alex")

        test_train.remove("Gosho")

        self.assertEqual(["Alex"], test_train.passengers)

    def test_remove_correct_return_message(self):

        test_train = Train("Thomas", 25)
        test_train.add("Gosho")
        test_train.add("Alex")

        self.assertEqual(test_train.remove("Alex"), "Removed Alex")


if __name__ == "__main__":
    main()



