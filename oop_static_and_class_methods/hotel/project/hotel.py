from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name

        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                # room.take_room(people)  # < -- here we need to put return, so the print isn't empty
                return room.take_room(people)  # < -- here we need to put return, so the print isn't empty

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()

    def find_guests(self):
        total_sum = 0
        for room in self.rooms:
            total_sum += room.guests

        return total_sum

    def status(self):
        result = f"Hotel {self.name} has {self.find_guests()} total guests\n"
        result += f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}\n"
        result += f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"
        return result

