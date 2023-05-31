from enum import Enum

class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        # todo
        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == Command.Action.WITHDRAW \
                and self.balance >= command.amount:
            self.balance -= command.amount
            command.success = True
        else:
            command.success = False

a = Account()

cmd = Command(Command.Action.DEPOSIT, 100)
a.process(cmd)

print(100, a.balance)
print(cmd.success)  # True

cmd = Command(Command.Action.WITHDRAW, 50)
a.process(cmd)

print(50, a.balance)
print(cmd.success)  # True

cmd.amount = 150
a.process(cmd)

print(50, a.balance)
print(cmd.success)  #False
