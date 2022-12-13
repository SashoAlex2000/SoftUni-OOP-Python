from project.animal import Animal
from project.mammal import Mammal

class Bear(Mammal):
    def __init__(self,name):
        super().__init__(name)