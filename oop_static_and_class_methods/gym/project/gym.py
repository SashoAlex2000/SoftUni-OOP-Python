

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []


    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def __find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity

    def subscription_info(self, subscriptipn_id):
        subscription = self.__find_by_id(self.subscriptions, subscriptipn_id)
        customer = self.__find_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_by_id(self.trainers, subscription.trainer_id)
        exercise_plan = self.__find_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_by_id(self.equipment, exercise_plan.equipment_id)

        return repr(subscription) + "\n" + \
            repr(customer) + "\n" + \
            repr(trainer) + "\n" + \
            repr(equipment) + "\n" + \
            repr(exercise_plan)







        # result = ""
        #
        # for subscription in self.subscriptions:
        #     if subscription.id == subscriptipn_id:
        #         result += f"{subscription}\n"
        #
        #         for customer in self.customers:
        #             if customer.id == subscription.customer_id:
        #                 result += f"{customer}\n"
        #
        #         for trainer in self.trainers:
        #             if trainer.id == subscription.trainer_id:
        #                 result += f"{trainer}\n"
        #
        #         for plan in self.plans:
        #             if plan.id == subscription.exercise_id:
        #                 for equip in self.equipment:
        #                     if equip.id == plan.equipment_id:
        #                         result += f"{equip}\n"
        #
        #                 result += f"{plan}\n"
        #
        #         return result


