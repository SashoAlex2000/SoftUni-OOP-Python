#START


class Customer:
    class_id = 1

    @classmethod
    def get_next_id(cls):
        cls.class_id += 1
        return cls.class_id - 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    def __repr__(self):
        return  f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


# test_customer = Customer("Alex", "mladost 1", "sahooo3@abv.bg")
# test_customer2 = Customer("Eli", "vitosha 1", "elenka@abv.bg")
# print(test_customer)
# print(test_customer2)
#
