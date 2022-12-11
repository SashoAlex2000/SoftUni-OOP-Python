# START

class Circle:
    def __init__(self, radius):
        self.radius = radius

    pi = 3.14

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return Circle.pi * self.radius * self.radius

    def get_circumference(self
                          ):
        return 2 * Circle.pi * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

print(Circle.pi)
# print(Circle.radius)   # < --- returns AttributeError - Circle has no attribute radius - since radius is an instance
# # attribute
