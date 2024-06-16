"""
Exclusive Or
The or operator returns a truthy value if either or both of its operands are truthy, a falsy value if both operands are falsy. The and operator returns a truthy value if both of its operands are truthy, and a falsy value if either operand is falsy. This works great until you need only one of two conditions to be truthy, the so-called exclusive or, also known as xor (pronounced "ECKS-or").

In this exercise, you will write an xor function that takes two arguments, and returns True if exactly one of its arguments is truthy, False otherwise.

Examples
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
"""
# def xor(arg1, arg2):
#     if arg1 and arg2:
#         return False
#     else:
#         return bool(arg1 or arg2)
    
# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

"""
or and and are so-called short circuit operators in that the second operand is not evaluated if its value is not needed. Does the xor function perform short-circuit evaluation of its operands? Why or why not? Does short-circuit evaluation in xor operations even make sense?
"""
# xor function doesn't perform short-circuit evaluation of its operands because its return value depends on evaluation of both operands. We wrote xor function to circumvent short-circuiting in the first place.


# Solution 2
def xor(arg1, arg2):
    return bool(arg1) != bool(arg2)

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)