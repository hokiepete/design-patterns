class Person:
    def __init__(self, age):
        self.age = age
        
    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'

class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    # todo: rest of this class
    @property
    def age(self):
        return self.person.age

    @age.setter
    def age(self, v):
        self.person.age = v
            
    def drink(self):
        if self.person.age >= 18:
            return self.person.drink()
        else:
            return "too young"

    def drive(self):
        if self.person.age >= 16:
            return self.person.drive()
        else:
            return "too young"
        
    def drink_and_drive(self):
        return "dead"

p = Person(10)
rp = ResponsiblePerson(p)

print('too young', rp.drive())
print('too young', rp.drink())
print('dead', rp.drink_and_drive())

rp.age = 20

print('driving', rp.drive())
print('drinking', rp.drink())
print('dead', rp.drink_and_drive())