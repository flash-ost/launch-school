def multiply(a, b):
    return a * b

def get_number(prompt):
    return float(input(prompt))

first = get_number('Enter the first number: ')
second = get_number('Enter the second number: ')

print(f'{first} * {second} = {multiply(first, second)}')