from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.animal import Animal


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        elif price > self.__budget:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary_payable = 0
        for worker in self.workers:
            total_salary_payable += worker.salary

        if total_salary_payable <= self.__budget:
            self.__budget -= total_salary_payable
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_tending = 0
        for animal in self.animals:
            total_money_for_tending += animal.money_for_care

        if total_money_for_tending <= self.__budget:
            self.__budget -= total_money_for_tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = ""
        result += f"You have {len(self.animals)} animals\n"
        # LIONS
        result += f"----- {len([animal for animal in self.animals if type(animal).__name__ == 'Lion'])} Lions:\n"

        for animal in self.animals:
            if type(animal).__name__ == "Lion":
                result += f"{animal.__repr__()}\n"

        # TIGERS
        result += f"----- {len([animal for animal in self.animals if type(animal).__name__ == 'Tiger'])} Tigers:\n"

        for animal in self.animals:
            if type(animal).__name__ == "Tiger":
                result += f"{animal.__repr__()}\n"

        # CHEETAHS
        result += f"----- {len([animal for animal in self.animals if type(animal).__name__ == 'Cheetah'])} Cheetahs:\n"
        cheetahs_printed = 0

        for animal in self.animals:
            cheetah_count = len([animal for animal in self.animals if type(animal).__name__ == 'Cheetah'])
            if type(animal).__name__ == "Cheetah":
                cheetahs_printed += 1
                if cheetahs_printed < cheetah_count:
                    result += f"{animal.__repr__()}\n"
                else:
                    result += f"{animal.__repr__()}"

        return result

    def workers_status(self):
        result = ""
        result += f"You have {len(self.workers)} workers\n"

        # KEEPERS
        result += f"----- {len([worker for worker in self.workers if type(worker).__name__ == 'Keeper'])} Keepers:\n"

        for worker in self.workers:
            if type(worker).__name__ == "Keeper":
                result += f"{worker.__repr__()}\n"

        # CARETAKERS

        result += f"----- {len([worker for worker in self.workers if type(worker).__name__ == 'Caretaker'])} Caretakers:\n"

        for worker in self.workers:
            if type(worker).__name__ == "Caretaker":
                result += f"{worker.__repr__()}\n"

        # VETS

        result += f"----- {len([worker for worker in self.workers if type(worker).__name__ == 'Vet'])} Vets:\n"
        vets_printed = 0

        for worker in self.workers:
            vet_count = len([worker for worker in self.workers if type(worker).__name__ == 'Vet'])

            if type(worker).__name__ == "Vet":
                vets_printed += 1
                if vets_printed < vet_count:
                    result += f"{worker.__repr__()}\n"
                else:
                    result += f"{worker.__repr__()}"

        return result

# lion_test = Lion("Morty", "male", 13)
# lion_test2 = Lion("djordji", "male", 11)
# tiger_test = Tiger("debeliq", "male", 69)
# print(lion_test.money_for_care)
# test_zoo = Zoo("test_zoo", 1000, 100, 100)
# print(test_zoo.add_animal(lion_test, 69))
# print(test_zoo.add_animal(lion_test2, 69))
# print(test_zoo.add_animal(tiger_test, 69))
# print(test_zoo.animal_status())
