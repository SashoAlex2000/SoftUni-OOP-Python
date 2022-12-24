class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):

    def test_is_initialized_correctly(self):
        integer = IntegerList()

        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_coorectly_wrong_data(self):
        integer = IntegerList("asd", 3.14)

        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_coorectly_integers(self):
        integer = IntegerList("asd", 3)

        self.assertEqual([3], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList("asd", 3)
        result = integer.get_data()

        self.assertEqual([3], result)

    def test_add_method_wrong_data(self):
        integer = IntegerList("asd", 3)

        with self.assertRaises(ValueError) as ex:
            integer.add("sus")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_method_correct_data(self):
        integer = IntegerList("asd", 3)

        integer.add(4)
        self.assertEqual([3, 4], integer._IntegerList__data)

    def test_remove_index_wrong_index(self):
        integer = IntegerList(2, 3)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_happy_case(self):
        integer = IntegerList(2, 3)
        integer.remove_index(0)

        self.assertEqual([3], integer._IntegerList__data)

    def test_returns_element_at_wanted_index(self):
        integer = IntegerList(2, 3)
        self.assertEqual(2, integer.remove_index(0))

    def test_get_happy_case(self):
        integer = IntegerList(2, 3)
        result = integer.get(0)

        self.assertEqual(2, result)

    def test_get_wrong_index(self):
        integer = IntegerList(2, 3)
        with self.assertRaises(IndexError) as ex:
            integer.get(2)

        self.assertEqual("Index is out of range", str(ex.exception))



    def test_insert_wrong_index(self):
        integer = IntegerList(2, 3)

        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 10)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_non_integer(self):
        integer = IntegerList(2, 3)

        with self.assertRaises(ValueError) as ex:
            integer.insert(1, "not an integer")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_happy_case(self):
        integer = IntegerList(2, 3)
        integer.insert(0, 10)

        self.assertEqual([10, 2, 3], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(2, 3, 100, 69, 101, -699)

        result = integer.get_biggest()

        self.assertEqual(101, result)

    def test_get_index(self):
        integer = IntegerList(2, 3, 100, 69, 101, -699)

        result = integer.get_index(100)

        self.assertEqual(2, result)


if __name__ == "__main__":
    main()

