import collections

# defaultdict accepts a class as a parameter
d = collections.defaultdict(collections.OrderedDict)
print(d['not in the dict'])
print(d['neither in the dict'])
print(d['this is the one'])

print(d)
"""
defaultdict(<class 'collections.OrderedDict'>, 
{'neither in the dict': OrderedDict(), 
 'not in the dict': OrderedDict(), 
 'this is the one': OrderedDict()})
"""

d['this is the one']['one'] = 'first'
d['this is the one']['two'] = 'second'
d['this is the one']['three'] = 'third'
d['this is the one']['four'] = 'fourth'

print(d['this is the one'])
"""
OrderedDict([('one', 'first'), ('two', 'second'), 
('three', 'third'), ('four', 'fourth')])
"""

class Calculator:
    """Incomplete calculator, it seems"""

    def __init__(self, op1, op2):
        self.operand1 = op1
        self.operand2 = op2

    def sum(self):
        return self.operand1 + self.operand2

    def subtract(self):
        return self.operand1 - self.operand2

ccc = Calculator(15, 12)

print(ccc.sum())
# 27
print(ccc.subtract())
# 3

def multiplication(self):
    return self.operand1 * self.operand2

Calculator.multiply = multiplication

print(ccc.multiply())
# 180

