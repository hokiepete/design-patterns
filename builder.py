class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.code = eval(f"{root_name}Builder()")

    def add_field(self, type, name):
        eval(f"self.code.add_{type}({name})")
        return self

    def __str__(self):
        return str(eval(f"self.code.{self.root_name.lower()}"))
        

class Person:
    def __init__(self):
        self.name = None
        self.age = None
        
    def __str__(self):
        return "class Person:\n  def  __init__(self):\n" \
            + f"    self.name = {self.name}\n" \
            + f"    self.age = {self.age}"
                

class PersonAgeBuilder:
    def __init__(self, person=Person()):
        self.person = person
        
    def add_age(self, age):
        self.person.age = age


class PersonBuilder(PersonAgeBuilder):
    def __init__(self, person=Person()):
        PersonAgeBuilder.__init__(self,person)
    
    def add_name(self, name):
        self.person.name = name


cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)