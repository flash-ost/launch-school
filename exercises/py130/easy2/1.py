"""
Default to a Period
Create a function greet that takes three arguments: a name, a greeting, and a punctuation mark, with the punctuation defaulting to a period.

Examples
print(greet("Antonina", "Hello")) # Hello, Antonina.
print(greet("Pete", "Good morning", "!")) # Good morning, Pete!
"""

def greet(name, greeting, mark='.'):
    return f'{greeting}, {name}{mark}'

print(greet("Antonina", "Hello")) # Hello, Antonina.
print(greet("Pete", "Good morning", "!")) # Good morning, Pete!