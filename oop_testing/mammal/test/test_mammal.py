from project.mammal import Mammal
from unittest import TestCase, main


class MammalTest(TestCase):

    def test_mammal_init_name(self):
        mammal = Mammal("Misho", "cat", "meow")

        self.assertEqual("Misho", mammal.name)

    def test_mammal_init_type(self):
        mammal = Mammal("Misho", "cat", "meow")

        self.assertEqual("cat", mammal.type)

    def test_mammal_init_sound(self):
        mammal = Mammal("Misho", "cat", "meow")

        self.assertEqual("meow", mammal.sound)

    def test_mammal_kingdom(self):
        #animals
        mammal = Mammal("Misho", "cat", "meow")

        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_mammal_make_sound(self):
        mammal = Mammal("Misho", "cat", "meow")
        result = mammal.make_sound()

        self.assertEqual(f"Misho makes meow", result)

    def test_mammal_get_kingdom(self):
        mammal = Mammal("Misho", "cat", "meow")
        result = mammal.get_kingdom()

        self.assertEqual("animals", result)

    def test_get_info(self):

        mammal = Mammal("Misho", "cat", "meow")
        result = mammal.info()

        self.assertEqual("Misho is of type cat", result)


if __name__ == "__main__":
    main()


