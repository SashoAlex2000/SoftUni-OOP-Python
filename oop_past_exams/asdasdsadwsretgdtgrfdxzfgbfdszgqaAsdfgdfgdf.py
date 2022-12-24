# import first_exam
#
#
#
#
# test_user = first_exam.project.user.User("Sasho", 22)
# # print(test_user.username)
# # test_user2 = User("", 22)
# # test_user = User("Sasho", 1)
# # test_thriller = movie_specification.thriller.Thriller("Django", 2013, test_user)
# print(test_user)

class TestClass():
    def __init__(self, cici):
        self.test_attr = cici

    def change_stuff(self, **kwargs):
        for key, value in kwargs.items():
            thing_to_change = key
            self.thing_to_change = value


test_case = TestClass("dupe")
print(test_case.test_attr)
test_case.change_stuff(test_attr="sasho")
print(test_case.test_attr)
