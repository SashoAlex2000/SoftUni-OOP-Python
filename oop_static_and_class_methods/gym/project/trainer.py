

class Trainer:
    class_id = 1

    @staticmethod
    def get_next_id():
        Trainer.class_id += 1
        return Trainer.class_id - 1

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"



