

class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = obj
        self.length = len(self.obj.keys()) - 1
        self.i = 0
        self.keys_list = [key for key in self.obj.keys()]


    def __iter__(self):
        return self

    def __next__(self):

        if self.i <= self.length:

            self.i += 1
            return self.keys_list[self.i-1], self.obj[self.keys_list[self.i-1]]

        else:
            raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


print(result.obj)
print(result.keys_list)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
