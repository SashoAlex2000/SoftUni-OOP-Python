from project.animal import Animal


class Lion(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 50)

# lion_test = Lion("Morty","male", 13)
# print(lion_test.money_for_care)