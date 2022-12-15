# START

def vowel_filter(function):
    def wrapper():
        result = []
        initial_list = function()
        for letter in initial_list:
            if letter.lower() in "aeiouy":
                result.append(letter)

        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
