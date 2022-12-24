from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    MAXIMUM_SPEED = 120
    SPEED_GAINED_TRAINING = 2

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.SPEED_GAINED_TRAINING > self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED
        else:
            self.speed += self.SPEED_GAINED_TRAINING


#
# test_appolosa = Appaloosa("cic", 100)
# test_appolosa.train()
# test_appolosa.train()
# test_appolosa.train()
# print(test_appolosa.speed)