

class Child():

    def __init__(self, food_cost, *args):

        self.cost = food_cost + sum(args)

#
# test_child = Child(10, 10,5,3)
# print(test_child.cost)