"""
Expand your answer to the previous program so it prints the result only when no exceptions are raised. You should also print End of the program regardless of whether an exception is raised.
"""
try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = num1 / num2
except ValueError:
    print('Invalid number.')
except ZeroDivisionError:
    print('Division by zero is invalid.')
else:
    print(f'Result: {result}')
finally:
    print('End of the program')    