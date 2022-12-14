from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name

        self.customers = []
        self.dvds = []

    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY
    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def __find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id ==entity_id:
                return entity

    def rent_dvd(self, customer_id, dvd_id):
        #
        # for customer in self.customers:
        #     for dvd in customer.rented_dvds:
        #         if dvd.id == dvd_id:
        #             if customer.id != customer_id:
        #                 return "DVD is already rented"
        #             elif customer.id == customer_id:
        #                 return f"{customer.name} has already rented {dvd.name}"
        #
        #     if customer.id == customer_id:
        #         searched_dvd = None
        #         for dvd in self.dvds:
        #             if dvd.id == dvd_id:
        #                 searched_dvd = dvd
        #
        #         if customer.age < searched_dvd.age_restriction:
        #             return f"{customer.name} should be at least {searched_dvd.age_restriction} to " \
        #                    f"rent this movie"
        #
        #         else:
        #             customer.rented_dvds.append(searched_dvd)
        #             for dvd in self.dvds:
        #                 if dvd.id == dvd_id:
        #                     dvd.is_rented = True
        #
        #             return f"{customer.name} has successfully rented {searched_dvd.name}"

        customer = self.__find_by_id(self.customers, customer_id)
        dvd = self.__find_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__find_by_id(self.customers, customer_id)
        dvd = self.__find_by_id(self.dvds, dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False

        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        # result = ""
        # for customer in self.customers:
        #     result += f"{customer}"
        #     result += "\n"
        #
        # for dvd in self.dvds:
        #     result += f"{dvd}"
        #     result += "\n"
        #
        # return result

        return "\n".join([repr(x) for x in self.customers]) + "\n" + "\n".join([repr(x) for x in self.dvds])



#
c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
#



