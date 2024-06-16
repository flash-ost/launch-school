"""
Logical Conditions 3
Without running the following code, determine what will be printed.

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")
"""

# Program will print 3.99. not operator flips the boolean value of an expression: not True => False => else block is executed.