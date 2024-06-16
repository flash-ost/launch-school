"""
Display Division
Without running the following code, determine what it will print:

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three
"""

# This is not a function invocation, so we won't see output from the block inside function definition.
# If we run the code from Python file, we will see nothing.
# If we run it line by line in Python REPL, we will see info about the function object.
def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three