

class Appliance():
    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        total_cost = self.cost * 30

        return total_cost


