"""
Modify your answer from the previous problem to raise a custom exception named NegativeNumberError instead of an ordinary ValueError exception.
"""
class NegativeNumberError(Exception):
    pass

num = float(input('Enter a number: '))
if num < 0:
    raise NegativeNumberError('Negative numbers are invalid.')
print(f'You entered: {num}')