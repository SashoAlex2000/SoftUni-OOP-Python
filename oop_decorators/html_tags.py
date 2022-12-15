#ASDASD


def tags(special_param):
    def decorator(func):
        def wrapper(*args):
            result = f"<{special_param}>"
            result += func(*args)
            result += f"</{special_param}>"
            return result
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))


