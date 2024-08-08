def double_odd_indexed(numbers):
    doubled_nums = []

    for index in range(len(numbers)):
        if index % 2 == 1:
            doubled_nums.append(numbers[index] * 2)
        else:
            doubled_nums.append(numbers[index])

    return doubled_nums

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_indexed(my_numbers))  # [2, 4, 6, 14, 2, 6]

# not mutated
print(my_numbers)     