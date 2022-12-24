from project.appliances.appliance import Appliance


class Laptop(Appliance):

    def __init__(self):
        super().__init__(1)


# test_fridge = Laptop()
# print(test_fridge.cost)
# print(test_fridge.get_monthly_expense())