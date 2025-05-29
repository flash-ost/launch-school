"""
Write a program that asks the user for two numbers and divides the first number by the second number. Handle any potential ZeroDivisionError or ValueError exceptions (there is no need to retry inputs in this problem).
"""
try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = num1 / num2
    print(f'Result: {result}')
except ValueError:
    print('Invalid number.')
except ZeroDivisionError:
    print('Division by zero is invalid.')
