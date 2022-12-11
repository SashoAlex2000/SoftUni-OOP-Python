#Done on the laptop!


class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def defend(self,amount):
        self.health -= amount

        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self,amount):
        self.health += amount
