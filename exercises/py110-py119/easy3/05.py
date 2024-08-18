"""
Reverse Number
Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

Examples
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
"""

## Understanding
# Input: positive integer
# Output: positive integer, with original integers' digits reversed

## Test Cases
# If original int ends with zeros, they should not be in return value (12000 -> 21)

## Data Structure
# No

## Algorithm
# Convert int to str
# Reverse
# Convert back to int and return

def reverse_number(num):
    return int(str(num)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True