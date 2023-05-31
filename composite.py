from abc import ABC
from collections.abc import Iterable

class Summer(ABC, Iterable):
    
    @property
    def sum(self):
        runing_sum = 0
        for s in self:
            if type(s) in [int, float]:
                runing_sum += s
            else:
                runing_sum += s.sum
        return runing_sum


class SingleValue(Summer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value

class ManyValues(list, Summer):
    pass

single_value = SingleValue(11)
other_values = ManyValues()
other_values.append(22)
other_values.append(33)
# make a list of all values
all_values = ManyValues()
all_values.append(single_value)
all_values.append(other_values)
print(all_values.sum, 66)