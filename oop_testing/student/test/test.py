# START

from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):

    def test_student_init_name(self):
        student = Student("Sasho")

        self.assertEqual("Sasho", student.name)

    def test_student_init_courses_nothing(self):
        student = Student("Sasho")

        self.assertEqual({}, student.courses)

    def test_student_init_courses_none(self):
        student = Student("Sasho", None)

        self.assertEqual({}, student.courses)

    def test_student_init_courses_some_info(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        self.assertEqual({"Python OOP": ["SOLID", "Encapsulation"]}, student.courses)

    def test_student_enroll_existing_course_return_statement(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        self.assertEqual("Course already added. Notes have been updated.", student.enroll("Python OOP", [], "N"))

    def test_student_enroll_existing_course_notes_update(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        student.enroll("Python OOP", ["Inheritance"], "N")

        self.assertEqual({"Python OOP": ["SOLID", "Encapsulation", "Inheritance"]}, student.courses)

    def test_student_enroll_new_course_addnotes_yes_return(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        self.assertEqual("Course and course notes have been added.",
                         student.enroll("Python Web", ["Django Introduction"], "Y"))

    def test_student_enroll_new_course_addnotes_yes_courses_update(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        student.enroll("Python Web", ["Django Introduction"], "Y")

        self.assertEqual({"Python OOP": ["SOLID", "Encapsulation"], "Python Web": ["Django Introduction"]},
                         student.courses)

    def test_student_enroll_new_course_addnotes_emptystring_return(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        self.assertEqual("Course and course notes have been added.",
                         student.enroll("Python Web", ["Django Introduction"], ""))

    def test_student_enroll_new_course_addnotes_emptystring_courses_update(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        student.enroll("Python Web", ["Django Introduction"], "")

        self.assertEqual({"Python OOP": ["SOLID", "Encapsulation"], "Python Web": ["Django Introduction"]},
                         student.courses)

    def test_student_enroll_new_course_no_addnotes_return(self):
        # Course has been added.
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        self.assertEqual("Course has been added.", student.enroll("Python Web", ["Django Introduction"], "NO"))

    def test_student_enroll_new_course_no_addnotes_courses(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        student.enroll("Python Web", ["Django Introduction"], "NO")

        self.assertEqual({"Python OOP": ["SOLID", "Encapsulation"], "Python Web": []}, student.courses)

    def test_students_add_notes_happy_case_return(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        self.assertEqual("Notes have been updated", student.add_notes("Python OOP", "Inheritance"))

    def test_students_add_notes_happy_case_courses_check(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        student.add_notes("Python OOP", "Inheritance")

        self.assertEqual({"Python OOP": ["SOLID", "Encapsulation", "Inheritance"]}, student.courses)

    def test_students_add_notes_course_not_found(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"]})

        with self.assertRaises(Exception) as ex:
            student.add_notes("Python Web", "Django Introduction")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_students_leave_course_happe_case_return(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"],"Python Web": ["Django Introduction"]})

        self.assertEqual("Course has been removed", student.leave_course("Python Web"))

    def test_students_leave_course_happe_case_courses_check(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"],"Python Web": ["Django Introduction"]})

        student.leave_course("Python Web")

        self.assertEqual({"Python OOP": ["SOLID", "Encapsulation"]}, student.courses)

    def test_students_leave_course_course_not_found(self):
        student = Student("Sasho", {"Python OOP": ["SOLID", "Encapsulation"],"Python Web": ["Django Introduction"]})

        with self.assertRaises(Exception) as ex:
            student.leave_course("JS Advanced")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()


