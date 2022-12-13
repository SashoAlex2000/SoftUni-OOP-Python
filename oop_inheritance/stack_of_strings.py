# START

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        # if len(self.data) == 0:
        #     return True
        # return False
        return len(self.data) == 0

    def __str__(self):
        # result = ""
        # result += "["
        # reversed_list = reversed(self.data)
        #
        # for el in reversed_list:
        #     result += f", {el}"
        # result += "]"
        # return result
        result = ""
        result += "["
        result += ", ".join(reversed(self.data))
        result += "]"

        return result


test_case = Stack()
test_case.push("as")
# test_case.push("asdas")
# test_case.push("ss")
# test_case.push("cxvxcv")
# test_case.push("123")
# test_case.push("alex")
print(test_case.pop())
print(test_case)
