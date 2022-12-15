# here with me <-- ???

class countdown_iterator():

    def __init__(self, count):
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.i:
            current = self.count
            self.count -= 1
            return current

        else:
            raise StopIteration


# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")


iterator1 = countdown_iterator(0)
for item in iterator1:
    print(item, end=" ")
