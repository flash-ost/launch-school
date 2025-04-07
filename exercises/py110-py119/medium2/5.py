"""
Next Featured Number Higher than a Given Value
A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

NOTE: The largest possible featured number is 9876543201.

Examples
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
"""
## Undersatnding
# Input: integer
# Output: integer (featured number) that satisfies the following conditions:
#   - should be greater than input number
#   - should be odd number
#   - should be multiple of 7
#   - all of its digits should occur exactly once

# The largest possible featured number is 9876543201.

## Algorithm:
# If input_num + 1 is greater than 9876543201:
#   return error message
# current_num = input_num + 1
# Create endless loop:
#   if current_num is odd and multiple of 7 and al of its digits occur once:
#       return current_num
#   current_num += 1

def next_featured(initial):
    current = initial + 1
    if current > 9876543201:
        return 'There is no possible number that fulfills those requirements.'
    
    while True:
        if current % 2 != 0 and current % 7 == 0 and len(str(current)) == len(set(str(current))):
            return current
        current += 1

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True