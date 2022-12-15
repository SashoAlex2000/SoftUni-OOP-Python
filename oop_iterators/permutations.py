from itertools import permutations


def possible_permutations(num_list):
    perm_obj = permutations(num_list)
    perm_list = list(perm_obj)
    final_list = []
    for element in perm_list:
        current_list = []
        for num in element:
            current_list.append(num)
        final_list.append(current_list)

    for cicka in final_list:
        yield(cicka)


[print(n) for n in possible_permutations([1, 2, 3])]
# print(possible_permutations([1, 2, 3]))
