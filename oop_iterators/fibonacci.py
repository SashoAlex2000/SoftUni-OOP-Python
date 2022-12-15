def fibonacci():
    result = [0, 1]
    yield result[-2]

    while True:
        yield result[-1]
        result.append(result[-2] + result[-1])


generator = fibonacci()
for i in range(15):
    print(next(generator))

print(generator.__next__())
# generator = fibonacci()
# for i in range(1):
#     print(next(generator))
