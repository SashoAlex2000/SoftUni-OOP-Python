

class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0
        self.cycles_done = 0
    def __iter__(self):
        return self

    def __next__(self):
        if (self.cycles_done * len(self.sequence)) + self.i < self.number:
            current = self.sequence[self.i]
            self.i += 1
            if self.i >= len(self.sequence):
                self.cycles_done += 1
                self.i = 0
            return current

        else:
            raise StopIteration


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

