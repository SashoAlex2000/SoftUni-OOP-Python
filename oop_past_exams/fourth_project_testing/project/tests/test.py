from project.library import Library

from unittest import TestCase, main

class LibraryTest(TestCase):

    def test_init_name_correct_initialization(self):
        test_library = Library("Aleksandria")

        self.assertEqual("Aleksandria", test_library.name)

    def test_init_name_incorrect_initialization(self):
        with self.assertRaises(ValueError) as ex:
            test_library = Library("")

        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_init_books_by_authors(self):
        test_library = Library("Aleksandria")

        self.assertEqual({}, test_library.books_by_authors)

    def test_init_readers(self):
        test_library = Library("Aleksandria")

        self.assertEqual({}, test_library.readers)

    def test_add_book_first_time(self):
        test_library = Library("Aleksandria")

        test_library.add_book("Michael Connolly", "Dirty Four")

        self.assertEqual(True, "Michael Connolly" in test_library.books_by_authors.keys())

    def test_add_book_first_time_book(self):
        test_library = Library("Aleksandria")

        test_library.add_book("Michael Connolly", "Dirty Four")

        self.assertEqual(["Dirty Four"], test_library.books_by_authors["Michael Connolly"])

    def test_add_book_second_time_repeating(self):
        test_library = Library("Aleksandria")

        test_library.add_book("Michael Connolly", "Dirty Four")
        test_library.add_book("Michael Connolly", "Dirty Four")

        self.assertEqual(["Dirty Four"], test_library.books_by_authors["Michael Connolly"])

    def test_add_book_second_time_successful(self):
        test_library = Library("Aleksandria")

        test_library.add_book("Michael Connolly", "Dirty Four")
        test_library.add_book("Michael Connolly", "The Lincoln Lawyer")

        self.assertEqual(["Dirty Four", "The Lincoln Lawyer"], test_library.books_by_authors["Michael Connolly"])

    def test_add_reader_correct(self):
        test_library = Library("Aleksandria")
        test_library.add_reader("Sasho")

        self.assertEqual(True, "Sasho" in test_library.readers.keys())

    def test_add_reader_repeating(self):
        test_library = Library("Aleksandria")
        test_library.add_reader("Sasho")

        self.assertEqual("Sasho is already registered in the Aleksandria library.", test_library.add_reader("Sasho"))

    def test_rent_book_no_such_user(self):
        test_library = Library("Aleksandria")

        test_library.add_book("Michael Connolly", "Dirty Four")

        result = test_library.rent_book("Sasho", "Michael Connolly", "Fair Warning")

        self.assertEqual("Sasho is not registered in the Aleksandria Library.", result)

    def test_rent_book_no_such_author(self):
        test_library = Library("Aleksandria")

        test_library.add_reader("Sasho")
        result = test_library.rent_book("Sasho", "Michael Connolly", "Fair Warning")

        self.assertEqual("Aleksandria Library does not have any Michael Connolly's books.", result)

    def test_rent_book_no_such_book(self):
        test_library = Library("Aleksandria")

        test_library.add_reader("Sasho")
        test_library.add_book("Michael Connolly", "Dirty Four")

        result = test_library.rent_book("Sasho", "Michael Connolly", "Fair Warning")

        self.assertEqual("""Aleksandria Library does not have Michael Connolly's "Fair Warning".""", result)



if __name__ == "__main__":
    main()