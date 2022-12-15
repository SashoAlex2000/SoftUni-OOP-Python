# START


def solution():
    def integers():
        i = 1
        while True:
            current = i
            i += 1
            yield current

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for _ in range(n):

            result.append(next(seq))
        return (result)

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(0, halves()))



