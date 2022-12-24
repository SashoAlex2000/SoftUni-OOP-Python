from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class StudentReportCardTest(TestCase):

    def test_init_name_correct(self):
        test_student = StudentReportCard("Alex", 3)

        self.assertEqual("Alex", test_student.student_name)

    def test_init_name_incorrect(self):
        with self.assertRaises(ValueError) as ex:
            test_student = StudentReportCard("", 3)

        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_init_school_year_correct(self):
        test_student = StudentReportCard("Alex", 3)

        self.assertEqual(3, test_student.school_year)

    def test_init_schoold_year_less_than_one(self):
        with self.assertRaises(ValueError) as ex:
            test_student = StudentReportCard("Alex", -5)

        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_init_schoold_year_more_than_twelve(self):
        with self.assertRaises(ValueError) as ex:
            test_student = StudentReportCard("Alex", 13)

        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_init_grades_dict(self):
        test_student = StudentReportCard("Alex", 3)

        self.assertEqual({}, test_student.grades_by_subject)

    def test_add_grade_new_subject(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 6)

        self.assertEqual({"Maths": [6]}, test_student.grades_by_subject)

    def test_add_grade_existing_subject(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 6)
        test_student.add_grade("Maths", 4)

        self.assertEqual({"Maths": [6, 4]}, test_student.grades_by_subject)

    def test_add_grade_second_subject(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 6)
        test_student.add_grade("Maths", 4)

        test_student.add_grade("Geography", 5)

        self.assertEqual({"Maths": [6, 4], "Geography": [5]}, test_student.grades_by_subject)

    def test_add_grade_second_subject_second_grade(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 6)
        test_student.add_grade("Maths", 4)

        test_student.add_grade("Geography", 5)
        test_student.add_grade("Geography", 6)

        self.assertEqual({"Maths": [6, 4], "Geography": [5, 6]}, test_student.grades_by_subject)

    def test_average_grade_by_subject(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 6)
        test_student.add_grade("Maths", 4)

        test_student.add_grade("Geography", 5)
        test_student.add_grade("Geography", 6)
        result = "Maths: 5.00\n"
        result += "Geography: 5.50"

        self.assertEqual(result, test_student.average_grade_by_subject())

    def test_average_grade_by_subject_second(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 6)
        test_student.add_grade("Maths", 4)

        result = "Maths: 5.00"

        self.assertEqual(result, test_student.average_grade_by_subject())

    def test_average_grade_by_subject_third(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 3)
        test_student.add_grade("Maths", 3)
        test_student.add_grade("Maths", 2)

        result = "Maths: 2.67"

        self.assertEqual(result, test_student.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 6)
        test_student.add_grade("Maths", 4)

        test_student.add_grade("Geography", 5)
        test_student.add_grade("Geography", 6)

        result = "Average Grade: 5.25"

        self.assertEqual(result, test_student.average_grade_for_all_subjects())

    def test_average_grade_for_all_subjects_second_time(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 6)
        test_student.add_grade("Maths", 4)

        test_student.add_grade("Geography", 5)
        test_student.add_grade("Geography", 6)
        test_student.add_grade("Geography", 6)
        test_student.add_grade("Geography", 6)

        result = "Average Grade: 5.50"

        self.assertEqual(result, test_student.average_grade_for_all_subjects())

    def test_average_grade_for_all_subjects_third(self):
        test_student = StudentReportCard("Alex", 3)

        test_student.add_grade("Maths", 6)
        test_student.add_grade("Maths", 4)
        test_student.add_grade("Maths", 3)

        test_student.add_grade("Geography", 5)
        test_student.add_grade("Geography", 6)
        test_student.add_grade("Geography", 5)

        result = "Average Grade: 4.83"

        self.assertEqual(result, test_student.average_grade_for_all_subjects())

    def test_report_card(self):
        test_student = StudentReportCard("Alex", 3)
        test_student.add_grade("Maths", 6)
        test_student.add_grade("Maths", 4)

        test_student.add_grade("Geography", 5)
        test_student.add_grade("Geography", 6)

        result = "Name: Alex\n"
        result += "Year: 3\n"
        result += "----------\n"
        result += "Maths: 5.00\n"
        result += "Geography: 5.50\n"
        result += "----------\n"
        result += "Average Grade: 5.25"

        self.assertEqual(result, test_student.__repr__())


if __name__ == "__main__":
    main()
