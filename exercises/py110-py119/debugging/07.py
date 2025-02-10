"""
Shadow
We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?

def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
"""
# We redefine a built-in sum function - so instead of using a built-in sum inside a new sum, we use a recursive call to new sum
# We should just change the name of our function
def sum_by_factor(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_by_factor(numbers, 2) == 20)