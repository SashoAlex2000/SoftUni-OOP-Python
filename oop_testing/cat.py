class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def test_size_after_eating(self):
        cat = Cat("Misho")

        cat.eat()
        self.assertEqual(1, cat.size)

    def test_fed_state_after_eating(self):
        cat = Cat("Misho")

        cat.eat()
        self.assertTrue(cat.fed)


    def test_if_already_fed(self):
        cat = Cat("Misho")
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))


    def test_falling_asleep_hungry(self):
        cat = Cat("Misho")
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


    def test_sleepiness_after_sleeping(self):
        cat = Cat("Misho")
        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()
