#start


def make_bold(function):
    def wrapper(*args):
        result = "<b>"
        result += f"{function(*args)}"
        result += "</b>"

        return result
    return wrapper

def make_italic(function):
    def wrapper(*args):
        result = "<i>"
        result += f"{function(*args)}"
        result += "</i>"

        return result
    return wrapper


def make_underline(function):
    def wrapper(*args):
        result = "<u>"
        result += f"{function(*args)}"
        result += "</u>"

        return result
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
