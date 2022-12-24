from project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTest(TestCase):

    def test_changing_books_sold(self):
        test_bookstore = Bookstore(12)

        with self.assertRaises(AttributeError) as ex:
            test_bookstore.total_sold_books = 5

        result = "can't set attribute"

        self.assertEqual(result, str(ex.exception))

    def test_init_books_limit_correct(self):
        test_bookstore = Bookstore(12)

        self.assertEqual(12, test_bookstore.books_limit)

    def test_init_book_limit_below_zero(self):
        with self.assertRaises(ValueError) as ex:
            test_bookstore = Bookstore(-5)

        self.assertEqual("Books limit of -5 is not valid", str(ex.exception))

    def test_init_book_limit_zero(self):
        with self.assertRaises(ValueError) as ex:
            test_bookstore = Bookstore(0)

        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_init_book_limit_not_int(self):
        with self.assertRaises(TypeError) as ex:
            test_bookstore = Bookstore("ccc")

        result = "'<=' not supported between instances of 'str' and 'int'"
        self.assertEqual(result, str(ex.exception))

    def test_init___total_sold_books(self):
        test_bookstore = Bookstore(12)

        # self.assertEqual(0, test_bookstore._Bookstore.__total_sold_books)
        self.assertEqual(0, test_bookstore.total_sold_books)

    def test_init_available_books(self):
        test_bookstore = Bookstore(12)

        self.assertEqual({}, test_bookstore.availability_in_store_by_book_titles)

    def test_len_bookstore(self):
        test_book_store = Bookstore(100)

        test_book_store.availability_in_store_by_book_titles = {"Nothing new on The Western Front": 50}

        self.assertEqual(50, len(test_book_store))

    def test_len_bookstore_second(self):
        test_book_store = Bookstore(100)

        test_book_store.availability_in_store_by_book_titles = {"Deadly Four": 2, "Memoar": 14}

        self.assertEqual(16, len(test_book_store))

    def test_receive_book_overload(self):
        test_book_store = Bookstore(10)

        test_book_store.receive_book("Deadly Four", 10)

        with self.assertRaises(Exception) as ex:
            test_book_store.receive_book("Deadly Four", 10)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_wrong_attr(self):
        test_book_store = Bookstore(10)

        with self.assertRaises(TypeError) as ex:
            test_book_store.receive_book("Deadly Four", "asd")

        result = "unsupported operand type(s) for +: 'int' and 'str'"

        self.assertEqual(result, str(ex.exception))

    def test_receive_book_in_the_edge(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)
        test_book_store.receive_book("CCC", 5)

        self.assertEqual({"CCC": 10}, test_book_store.availability_in_store_by_book_titles)


    def test_receive_book_correct_new_book(self):
        test_book_store = Bookstore(10)

        test_book_store.receive_book("CCC", 5)

        self.assertEqual({"CCC": 5}, test_book_store.availability_in_store_by_book_titles)

    def test_receive_book_correct_return(self):
        test_book_store = Bookstore(10)

        result = "5 copies of CCC are available in the bookstore."

        self.assertEqual(result, test_book_store.receive_book("CCC", 5))

    def test_receive_book_correct_second_book(self):
        test_book_store = Bookstore(10)

        test_book_store.receive_book("CCC", 5)
        test_book_store.receive_book("AAA", 3)

        self.assertEqual({"CCC": 5, "AAA": 3}, test_book_store.availability_in_store_by_book_titles)

    def test_receive_book_second_correct_return(self):
        test_book_store = Bookstore(10)

        test_book_store.receive_book("CCC", 5)
        result = "3 copies of AAA are available in the bookstore."

        self.assertEqual(result, test_book_store.receive_book("AAA", 3))

    def test_receive_book_correct_existing_book(self):
        test_book_store = Bookstore(10)

        test_book_store.receive_book("CCC", 5)
        test_book_store.receive_book("CCC", 3)

        self.assertEqual({"CCC": 8}, test_book_store.availability_in_store_by_book_titles)

    def test_receive_book_correct_existing_book_return(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)

        result = "8 copies of CCC are available in the bookstore."

        self.assertEqual(result, test_book_store.receive_book("CCC", 3))

    def test_receive_book_existing_book(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)
        test_book_store.receive_book("CCC", 3)

        self.assertEqual({"CCC": 8}, test_book_store.availability_in_store_by_book_titles)

    def test_receive_book_again_again(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)
        test_book_store.receive_book("AAA", 3)
        test_book_store.receive_book("CCC", 1)

        self.assertEqual({"CCC": 6, "AAA": 3}, test_book_store.availability_in_store_by_book_titles)

    def test_sell_book_not_exist(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)

        with self.assertRaises(Exception) as ex:
            test_book_store.sell_book("AAA", 3)

        result = "Book AAA doesn't exist!"

        self.assertEqual(result, str(ex.exception))

    def test_sell_book_not_enough_books(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)

        with self.assertRaises(Exception) as ex:
            test_book_store.sell_book("CCC", 6)

        result = "CCC has not enough copies to sell. Left: 5"

        self.assertEqual(result, str(ex.exception))

    def test_successfull_sale_availability(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)

        test_book_store.sell_book("CCC", 3)

        self.assertEqual({"CCC": 2}, test_book_store.availability_in_store_by_book_titles)

    def test_successfull_sale_books_sold(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)

        test_book_store.sell_book("CCC", 3)

        self.assertEqual(3, test_book_store.total_sold_books)

    def test_successfull_sale_test_len(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)

        test_book_store.sell_book("CCC", 3)

        self.assertEqual(2, len(test_book_store))

    def test_successful_sale_return(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)

        result = "Sold 3 copies of CCC"

        self.assertEqual(result, test_book_store.sell_book("CCC", 3))

    def test_successful_sale_multiple_books(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)
        test_book_store.receive_book("AAA", 3)
        test_book_store.receive_book("BBB", 1)

        test_book_store.sell_book("AAA", 2)
        test_book_store.sell_book("CCC", 3)

        self.assertEqual({"CCC": 2, "AAA": 1, "BBB": 1}, test_book_store.availability_in_store_by_book_titles)

    def test_succ_sale_reaches_zero(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)
        test_book_store.sell_book("CCC", 5)

        self.assertEqual({"CCC": 0}, test_book_store.availability_in_store_by_book_titles)

    def test_succ_sale_reaches_zero_len(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)
        test_book_store.sell_book("CCC", 5)

        self.assertEqual(0, len(test_book_store))

    def test_successful_sale_multiple_books_books_sold(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)
        test_book_store.receive_book("AAA", 3)
        test_book_store.receive_book("BBB", 1)

        test_book_store.sell_book("AAA", 2)
        test_book_store.sell_book("CCC", 3)

        self.assertEqual(5, test_book_store.total_sold_books)

    def test_successful_sale_multiple_books_availability(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)
        test_book_store.receive_book("AAA", 3)
        test_book_store.receive_book("BBB", 1)

        test_book_store.sell_book("AAA", 2)
        test_book_store.sell_book("CCC", 3)

        self.assertEqual(4, len(test_book_store))

    def test_string_first(self):
        # result = "Sold 20 copies of CCC\n"
        result = "Total sold books: 20\n"
        result += "Current availability: 40\n"
        result += " - CCC: 40 copies"

        test_book_store = Bookstore(100)
        test_book_store.availability_in_store_by_book_titles = {"CCC": 50}
        test_book_store.receive_book("CCC", 10)
        test_book_store.sell_book("CCC", 20)

        self.assertEqual(result, test_book_store.__str__())

    def test_string_new_store(self):
        result = "Total sold books: 0\n"
        result += "Current availability: 0"
        test_book_store = Bookstore(100)

        self.assertEqual(result, test_book_store.__str__())

    def test_string_third_time(self):
        test_book_store = Bookstore(10)
        test_book_store.receive_book("CCC", 5)
        test_book_store.receive_book("AAA", 3)
        test_book_store.receive_book("BBB", 1)

        test_book_store.sell_book("AAA", 2)
        test_book_store.sell_book("CCC", 3)

        result = "Total sold books: 5\n"
        result += "Current availability: 4\n"
        result += " - CCC: 2 copies\n"
        result += " - AAA: 1 copies\n"
        result += " - BBB: 1 copies"

        self.assertEqual(result, test_book_store.__str__())


if __name__ == "__main__":
    main()
