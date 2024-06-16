"""
Floating Point Arithmetic
Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

Examples
==> Enter the first number:
3.141529
==> Enter the second number:
2.718282
==> 3.141529 + 2.718282 = 5.859811
==> 3.141529 - 2.718282 = 0.42324699999999993
==> 3.141529 * 2.718282 = 8.539561733178
==> 3.141529 / 2.718282 = 1.1557038600115808
==> 3.141529 // 2.718282 = 1.0
==> 3.141529 % 2.718282 = 0.42324699999999993
==> 3.141529 ** 2.718282 = 22.45792517468373
"""
# Solution 1
# def prompt(message):
#     print(f'==>{message}')

# prompt('Enter the first number:')
# num1 = float(input())

# prompt('Enter the second number:')
# num2 = float(input())

# prompt(f'{num1} + {num2} = {num1 + num2}')
# prompt(f'{num1} - {num2} = {num1 - num2}')
# prompt(f'{num1} * {num2} = {num1 * num2}')
# prompt(f'{num1} / {num2} = {num1 / num2}')
# prompt(f'{num1} // {num2} = {num1 // num2}')
# prompt(f'{num1} % {num2} = {num1 % num2}')
# prompt(f'{num1} ** {num2} = {num1 ** num2}')

# Solution 2
def prompt(message):
    print(f'==> {message}')

def calculate(first, second, operator):
    match operator:
        case '+': return first + second
        case '-': return first - second
        case '*': return first * second
        case '/': return first / second
        case '//': return first // second
        case '%': return first % second
        case '**': return first ** second

prompt('Enter the first number:')
num1 = float(input())

prompt('Enter the second number:')
num2 = float(input())

for operator in ['+', '-', '*', '/', '//', '%', '**']:
    prompt(f'{num1} {operator} {num2} = {calculate (num1, num2, operator)}')