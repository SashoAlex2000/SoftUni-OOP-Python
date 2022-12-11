#DONE on the laptop

class Employee:
    def __init__(self,id,first_name,last_name,salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def raise_salary(self,amount_of_raise):
        self.salary += amount_of_raise
        return self.salary

    def get_annual_salary(self):
        return self.salary*12
