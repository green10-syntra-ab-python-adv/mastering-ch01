import collections, types, copy


class Calculator(object):
    """Incomplete calculator, it seems"""

    def __init__(self):
        self.operand1 = 15
        self.operand2 = 12

    def sum(self):
        return self.operand1 + self.operand2

    def subtract(self):
        return self.operand1 - self.operand2


# defaultdict accepts a class as a parameter
d = collections.defaultdict(Calculator)


d['plus-minus']  # object created thanks to defaultdict


def multiplication(self):
    return self.operand1 * self.operand2


d['plus-minus-times'].multiply = \
    types.MethodType(multiplication, d['plus-minus-times'])


def division(self):
    return self.operand1 / self.operand2


# clone object
d['plus-minus-times-divided'] = copy.copy(d['plus-minus-times'])

d['plus-minus-times-divided'].divide = \
    types.MethodType(division, d['plus-minus-times-divided'])


print(d['plus-minus'].sum())
print(d['plus-minus'].subtract())
"""
27
3
"""

print(d['plus-minus-times'].sum())
print(d['plus-minus-times'].subtract())
print(d['plus-minus-times'].multiply())
"""
27
3
180
"""

print(d['plus-minus-times-divided'].sum())
print(d['plus-minus-times-divided'].subtract())
print(d['plus-minus-times-divided'].multiply())
print(d['plus-minus-times-divided'].divide())
"""
27
3
180
1.25
"""


