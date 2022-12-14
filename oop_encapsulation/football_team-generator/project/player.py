#START

class Player:
    def __init__(self,name,sprint,dribble,passing,shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name


    def __str__(self):
        return f"Player: {self.__name}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}"
#
# test_player = Player("max",28,99,77,11)
# print(test_player)