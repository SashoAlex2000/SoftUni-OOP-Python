

class Equipment():
    class_id = 1

    @staticmethod
    def get_next_id():
        result = Equipment.class_id
        Equipment.class_id += 1
        return result

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"


# test_eq = Equipment("peckdeck")
# test_eq2 = Equipment("bench press")
# print(test_eq)
# print(test_eq2)