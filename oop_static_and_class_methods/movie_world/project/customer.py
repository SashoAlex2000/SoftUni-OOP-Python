#START

class Customer():
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented" \
               f" DVD's ({', '.join([dvd.name for dvd in self.rented_dvds])})"



# test_customer = Customer("ales", 22, 1234)
# print(test_customer)