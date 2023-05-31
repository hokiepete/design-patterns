class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.participants.append(self)

    def say(self, value):
        # todo
        self.mediator.broadcast(self, value)
    
    def update_value(self, value):
        self.value += value

class Mediator:
    def __init__(self):
        self.participants = []
        
    def broadcast(self, sender, value):
        for participant in self.participants:
            if participant is not sender:
                participant.update_value(value)

m = Mediator()
p1 = Participant(m)
p2 = Participant(m)

print(0, p1.value)
print(0, p2.value)

p1.say(2)

print(0, p1.value)
print(2, p2.value)

p2.say(4)

print(4, p1.value)
print(2, p2.value)