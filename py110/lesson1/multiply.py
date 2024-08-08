def multiply(numbers, multiplier):
    multiplied = [number * multiplier for number in numbers]
    return multiplied

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]