from project.appliances.appliance import Appliance


class Fridge(Appliance):

    def __init__(self):
        super().__init__(1.2)


# test_fridge = Fridge()
# print(test_fridge.cost)
# print(test_fridge.get_monthly_expense())