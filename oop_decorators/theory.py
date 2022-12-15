import random


def uppercase(function):
    def wrapper(giggdy):
        result = function(giggdy)
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


@uppercase
def say_slur(slur_list):
    current_word = random.choice(slur_list)
    # current_word = "faggot"

    return current_word


gamer_moments = ["faggot", "n00b.", "ciganin"]

print(say_slur(gamer_moments))


def test_func():
    return ("testing...")

test_dict = {}

test_func.self_dict = test_dict
print(test_func.self_dict)