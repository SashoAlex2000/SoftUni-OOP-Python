from project.animal import Animal
from project.reptile import Reptile

class Lizard(Reptile):
    def __init__(self,name):
        super().__init__(name)