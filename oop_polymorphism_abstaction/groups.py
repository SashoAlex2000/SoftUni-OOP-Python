class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, *args):
        self.name = name
        self.people = [person for person in args[0]]

    def __len__(self):
        return len(self.people)

    def __add__(self, other):

        new_list = []
        for person in self.people: new_list.append(person)
        for person in other.people: new_list.append(person)
        print(new_list)
        return Group(f"{self.name} {other.name}", new_list)

    def __repr__(self):
        # return f"Group {self.name} with members {' '.join(member.__repr__ for member in self.people)}"
        # result = f"Group {self.name}"
        # for person in self.people:
        #     result += f", {person}"
        #
        # return result

        return f"Group {self.name} with members " + ", ".join(f'{person}' for person in self.people)

    def __iter__(self):
        new_people = [f"Person {self.people.index(person)} {person}" for person in self.people]
        return iter(new_people)

    def __getitem__(self, item:int):
        wanted_person = self.people[item]
        return f"Person {self.people.index(wanted_person)} {wanted_person}"

p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
