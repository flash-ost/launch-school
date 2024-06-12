"""
Sum or Product of Consecutive Integers
Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

Example 1
Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.
Example 2
Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.
"""
ALLOWED_OPERATIONS = ['s', 'p']
integer = 0
while integer < 1:
    integer = int(input('Please enter an integer greater than 0: '))

operation = None
while operation not in ALLOWED_OPERATIONS:
    operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')

if operation == 's':
    print(f'The sum of the integers between 1 and {integer} is {sum(range(1, integer + 1))}.')
else:
    product = 1
    for number in range(1, integer + 1):
        product *= number
    print(f'The product of the integers between 1 and {integer} is {product}.')
