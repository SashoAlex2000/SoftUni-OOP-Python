from project.animal import Animal
from project.mammal import Mammal

class Gorilla(Mammal):
    def __init__(self,name):
        super().__init__(name)