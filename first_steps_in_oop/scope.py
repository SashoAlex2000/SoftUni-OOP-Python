from math import sqrt

b = 100

print(b)

def sum_nums():
    # global b  # <--- makes the b from the local scope global hereinafter; BAD PRACTICE! 
    a = 5
    b = 11
    print(b)  # < ---takes local 'b'
    return a + b


print(sum_nums())
print(b)  # <--- takes global 'b'
# print(a)   <--- cannot do that, 'a' is not defined


# def print():
#     pass
# print(__name__)  # <--- print takes 0 positional arguments; print is taken from the global scope first



# def sqrt():   # <--- function sqrt at 0x04... vs build-in function sqrt()
#     pass
# print(sqrt(5))    # <--- takes 0 positional arguments
