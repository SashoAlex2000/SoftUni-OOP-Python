

class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):

        # if value == "" or value == " ":
        # if value.replace(" ", "") == "":
        if not value:
            raise ValueError("The topping type cannot be an empty string")

        self.__topping_type = value
        

# test_topping = Topping("salami",14)
# # test_topping3 = Topping("salami",-85541)
# test_topping2 = Topping("         ",14)
# print(test_topping.topping_type)
# print(test_topping2.topping_type)
# print(test_topping.weight)
