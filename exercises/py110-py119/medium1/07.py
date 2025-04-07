"""
Fibonacci Numbers (Procedural)
The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)
Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to the function:

Examples
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

If you're familiar with the concept of recursive functions, don't try to write a recursive solution at this time; you'll do that in the next exercise. In other words, write a procedural function that doesn't try to call itself.

If you don't know about or understand recursion, don't worry about it. You'll learn soon enough.
"""

## Understanding
# Input: integer (n)
# Output: integer representing the last number in Fibonacci sequence of length set by input integer

# Explicit rules
# - don't use recursion

## Algorithm
# Set previous_num and current_num to 1
# Iterate over range from 2 to n
#   store value of current_num in tmp
#   assign current_num a new value, adding previous_num and current_num
#   assign previous_num a value from tmp
# Return current_num

def fibonacci(n):
    previous = 1
    current = 1
    for _ in range(2, n):
        previous, current = current, current + previous
    return current

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True