class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    idx = 0
    def create_person(self, name):
        person = Person(self.idx, name)
        PersonFactory.idx += 1
        return person

alan = PersonFactory().create_person('alan')
bob = PersonFactory().create_person('bob')
print(alan.id)
print(bob.id)