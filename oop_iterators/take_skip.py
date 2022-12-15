#START


class take_skip():
    def __init__(self, step, count):
        self.step = step
        self.count = count

    iterations_done = 0
    current_num = 0

    def __iter__(self):
        return self

    def __next__(self):


        if self.iterations_done < self.count:
            current = self.current_num
            self.current_num += self.step
            self.iterations_done += 1
            return current

        else:
            raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
