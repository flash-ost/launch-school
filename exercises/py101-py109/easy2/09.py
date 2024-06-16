"""
How Old is Teddy?
Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

Example Output
Teddy is 69 years old!
"""
from random import randint, randrange

# print(f'Teddy is {randrange(20, 101)} years old!')

name = input('Enter a name: ') or 'Teddy'
print(f'{name} is {randint(20, 100)} years old!')