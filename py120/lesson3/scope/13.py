"""
Consider the following code:

class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"
Answer the following question without running the code.

When an instance of Pine is created, what value will its type attribute have? Why?
"""
# Its type attribute will have value 'Pine Tree'.
# By calling super().__init__() we first set it to 'Generic Tree',
# but on the next line reassign to 'Pine Tree'.

class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

pine = Pine()
print(pine.type)        