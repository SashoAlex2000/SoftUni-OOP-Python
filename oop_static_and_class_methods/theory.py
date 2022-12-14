# import math
#
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
#     def calculate_distance(self, point):
#         return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)
#
#     @staticmethod
#     def cal_distance(point1, point2):
#         return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
#
# p = Point(5,6)
# p2 = Point(3,4)
# print(p.calculate_distance(p2))
# print(Point.cal_distance(p, p2))
#
#
# class Laptop:
#     def __init__(self, memory, model):
#         self.memory = memory
#         self.model = model
#     brand = "Asus"
#
#     @classmethod
#     def lor_ram_laptop(cls):
#         return cls(8, "ASUS")
#
#     @classmethod
#     def high_ram_laptop(cls):
#         return cls(32, "ASUS")
#
#     @classmethod
#     def change_brand(cls):
#         cls.brand = "changed"
#
# small_ram_laptop = Laptop.lor_ram_laptop()
# high_ram_laptop = Laptop.high_ram_laptop()
# print(small_ram_laptop.memory)
# print(high_ram_laptop.memory)
# print(small_ram_laptop)
#
# print(Laptop.brand)
# Laptop.change_brand()
# print(Laptop.brand)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
#
# girl = Person("Lilly", 14)
# print(Person.is_adult((girl.age)))
import calendar
cici = "03"
print(calendar.month_name(int(cici)))