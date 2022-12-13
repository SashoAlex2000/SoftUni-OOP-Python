class Person:
    def __init__(self, name, age):
        if len(name.split()) < 2:
            raise Exception("Please specify at least two names")
        result = [len(n) >= 2 for n in name.split()]
        if not all(result):
            raise Exception("Each name must be at least two characters")  # < --- not done in the constructor usually
        self.name = name
        if age <= 0:
            raise Exception("Age must be bigger than 0")
        self.age = age

    def __str__(self):
        return f"{self.name}, age: {self.age}"


class Employee(Person):
    def __init__(self, name, age, work_id, salary):
        super().__init__(name, age)
        if work_id < 3:
            raise Exception("Invalid work ID format")
        self.work_id = work_id
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, age, work_id, salary, commission):
        super().__init__(name, age, work_id, salary)
        self.commission = commission


person = Person("TEST TESTOV", 69)
print(person)
# person2 = Person("c cuckov",22)   # < --- return an error, due to the first name being 1 character
a = 4
employee = Employee("My name", 20, 1111, 3000)
print(employee)

# employee2 = Employee("EMPL TWO",-1,1111,3000)
print(employee.__repr__())  # < --- not defined in daughter/parent class - so it goes to object


# print(employee.commission)  # < ---attribute error, since employee cannot inherit "down" from manager

class Car:
    def __init__(self, model="Audi"):
        self.gadgets = []
        self.model = model


class SportsCar(Car):
    def __init__(self, nickname):
        super().__init__()
        self.nickname = nickname


sport_car = SportsCar("Fast&Furious")
print(sport_car.nickname)
print(sport_car.gadgets)
print(sport_car.model)
