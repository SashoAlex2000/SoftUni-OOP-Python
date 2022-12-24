from project.rooms.room import Room


class AloneOld(Room):

    def __init__(self, family_name, pension):

        super().__init__(family_name, pension, 1)
        self.room_cost = 10


# test_aloneold = AloneOld("Petrov", 450)
# print(test_aloneold.budget)
# print(test_aloneold.members_count)
# print(test_aloneold.calculate_expenses())

