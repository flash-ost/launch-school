"""
Fibonacci Numbers (Memoization)
Our recursive fibonacci function from the previous exercise isn't very efficient. It starts slowing down with an nth argument value somewhere around 35-60, depending on your system. One way to improve the performance of our recursive fibonacci function (and other recursive functions) is to use memoization.

Memoization is an approach that involves saving a computed answer for future reuse, instead of computing it from scratch every time it is needed. In the case of our recursive fibonacci function, using memoization saves calls to fibonacci(nth - 2) because the necessary values have already been computed by the recursive calls to fibonacci(nth - 1).

For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.

Fibonacci Memoization

Hint: One approach to memoization is to use a lookup table, such as an object, for storing and accessing previously computed values.
"""

## Understanding
# Input: integer (n)
# Output: integer representing the last number in Fibonacci sequence of length set by input integer

# Explicit rules
# - use recursion and memoization

## Algorithm
# Create a loolup table outsude of function with base case numbers (1, 2) as keys and 1 as value
# Recursive function to calculate Fibonacci number:
# Base case
#   if n is among table keys, return corresponding value
# Recursive case
#   store a new key-value pair in table with n as key and 
#   'return value of recursive function call with n - 1 as an argument + call with n - 2 as argument' as value
#   return table value corresponding to key n

table = { 1: 1, 2: 1 }
def fibonacci(n):
    # Base case
    if n in table:
        return table[n]
    
    # Recursive case
    table[n] = fibonacci(n-1) + fibonacci(n-2)
    return table[n]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True