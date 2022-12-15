
def number_increment(numbes):

    def increase():
        new_list = []
        for num in numbes:
            new_list.append(num+1)

        return new_list

    return increase()

print(number_increment([1, 2, 3]))

