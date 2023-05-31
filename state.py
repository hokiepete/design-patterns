class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.combination = ''.join([str(x) for x in combination])
        # todo
    
    def reset(self):
        # todo - reset lock to LOCKED state
        self.status = 'LOCKED'

    def enter_digit(self, digit):
        # todo
        if self.status == 'ERROR':
            return

        if self.status == 'LOCKED':
            self.status = str(digit)
        else:
            self.status += str(digit)
        
        if self.status == self.combination:
            self.status = 'OPEN'
        elif len(self.status) == len(str(self.combination)):
            self.status = 'ERROR'
        

cl = CombinationLock([1, 2, 3, 4, 5])
print('LOCKED', cl.status)
cl.enter_digit(1)
print('1', cl.status)
cl.enter_digit(2)
print('12', cl.status)
cl.enter_digit(3)
print('123', cl.status)
cl.enter_digit(4)
print('1234', cl.status)
cl.enter_digit(5)
print('OPEN', cl.status)


cl = CombinationLock([1, 2, 3])
print('LOCKED', cl.status)
cl.enter_digit(1)
print('1', cl.status)
cl.enter_digit(2)
print('12', cl.status)
cl.enter_digit(5)
print('ERROR', cl.status)
