from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    MAXIMUM_SPEED = 140
    SPEED_GAINED_TRAINING = 3

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.SPEED_GAINED_TRAINING > self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED
        else:
            self.speed += self.SPEED_GAINED_TRAINING


# test_horsey = Thoroughbred("CCCCC", 139)
# test_horsey.train()
# test_horsey.train()
# test_horsey.train()
# test_horsey.train()
# print(test_horsey.speed)
