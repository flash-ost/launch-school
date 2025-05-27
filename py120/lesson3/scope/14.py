"""
Consider the following code:

class A:
    def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)
"""
# AttributeError. Class B overrides init of class A with its own,
# where we only initialize attribute var_b.
class A:
    def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)
