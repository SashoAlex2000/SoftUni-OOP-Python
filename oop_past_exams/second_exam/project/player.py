

class Player():
    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.already_used_names.append(name)

    already_used_names = []
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        test_value = " ".join([ch for ch in value if ch != " "])
        if test_value == " ":
            raise ValueError("Name not valid!")
        if value == " ":
            raise ValueError("Name not valid!")

        if value in self.already_used_names:
            raise Exception(f"Name {value} is already used!")

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        if self.stamina < 100:
            return True
        return False

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

#
# test_player = Player("Sasho", 22, 100)
# print(test_player.name)
# print(Player.already_used_names)
# test_player2 = Player("Gosho", 12, 13)
# print(test_player2.stamina)
# print(test_player2.need_sustenance)
# print(test_player2)

