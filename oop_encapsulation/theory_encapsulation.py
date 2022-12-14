class CreditCard:
    def __init__(self, number, exp_date, cvv, name, pin):
        self.number = number
        self.exp_date = exp_date
        self._cvv = cvv
        self.name = name
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin


class ChildCreditCard(CreditCard):
    def __init__(self, number, exp_date, cvv, name, pin, child_name):
        super().__init__(number, exp_date, cvv, name, pin)
        self.child_name = child_name


card = CreditCard(1236969420696969, "2022-10", 111, "Malinov", 7887)
print(card._CreditCard__pin)
card._CreditCard__pin = 6969
print(card._CreditCard__pin)

class Person:
    def __init__(self, age=0):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age < 18: self.__age = 18
        else: self.__age = age

test_person = Person(4)
print(test_person.age)


class Car:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def drive(self):
        print('driving max speed ' + str(self.max_speed))

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value > 447:
            value = 447
        self.__max_speed = value

red_car = Car(200)
red_car.drive()             # driving max speed 200
red_car.max_speed = 512     # changes the speed to 447
red_car.drive()

#################################################################

class Person:
    def __init__(self):
        self.first_name = 'Peter'
        self.last_name = 'Parker'

    def __full_name(self):
        return f'{self.first_name} {self.last_name}'

    def info(self):
        return self.__full_name()

person = Person()
print(person.info())	              # Peter Parker
# print(person.__full_name())	   # AttributeError
print(person._Person__full_name())  # Peter Parker

