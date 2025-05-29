"""
Write a function that takes a list of numbers and returns the inverse of each number (if n is a number, then 1 / n is its inverse). Handle any exceptions that might occur.
"""
def invert(nums):
    result = []
    for num in nums:
        try:
            result.append(1 / num)
        except ZeroDivisionError:
            result.append(float('inf'))
    return result

lst1 = [1, 2, 3]
lst2 = [0, 1, 2]

print(invert(lst1))
print(invert(lst2))