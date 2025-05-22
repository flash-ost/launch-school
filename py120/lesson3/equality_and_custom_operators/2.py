"""
Consider the following class:

class Cat:
    def __init__(self, name):
        self.name = name
Create the methods needed so you can compare Cat objects for equality and inequality by their name value. The comparisons should ignore case and should work for the == and != operators. If the right-hand operand is not a Cat object, the methods should return NotImplemented.

Be sure to write test cases to demonstrate that your methods work as intended.
"""
class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() != other.name.casefold()
    
upperjack = Cat('Jack')
lowerjack = Cat('jack')
jam = Cat('Jam')

# All should print True
print((upperjack == lowerjack) == True)
print((upperjack != lowerjack) == False)

print((upperjack == jam) == False)
print((upperjack != jam) == True)

print((upperjack == 'Jack') == False)
print((upperjack != 'Jack') == True)
