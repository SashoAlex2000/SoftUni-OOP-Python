#AAA


def logged(func):
    def wrapped(*args):
        func_result = func(*args)
        result = ""
        result += f"you called {func.__name__}({', '.join([str(arg) for arg in args])})\n"
        result += f"it returned {func_result}"
        return result
    return wrapped


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
