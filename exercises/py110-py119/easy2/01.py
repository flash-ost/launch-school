"""
Cute Angles
Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:

DEGREE = "\u00B0"

Examples
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
"""

## Understanding
# Input: float representing angle between 0 and 360 degrees
# Output: string with provided float written as degrees, minutes and seconds, properly formatted
# Explicit rules:
# - degree symbol (°) for degrees, a single quote (') for minutes, and a double quote (") for seconds
# - there are 60 minutes in a degree, and 60 seconds in a minute.

## Examples
# Minutes and seconds should always consist of 2 digits, even if input is 0

## Data Structure
# No for this task

## Algorithm
# Store flooe part in var
# Separate fractional part from float by subtracting floor part
# Divide separated fractional part by 100 and multiply by 60. Store floor part of result in var minutes.
# Separate fractional part of result, multiply by 6
# Create a string with proper formatting
# Return string

"""
Further Exploration
Can you refactor the function so that it works with any positive or negative number?

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"
"""

def dms(degrees_float):
    DEGREE = "\u00B0"
    MIN_IN_DEGREE = 60
    SEC_IN_MIN = 60

    if degrees_float < 0 or degrees_float > 360:
        degrees_float %= 360

    degrees = int(degrees_float)
    minutes = int(degrees_float % 1 * MIN_IN_DEGREE)
    seconds = int(((degrees_float % 1 * MIN_IN_DEGREE)) % 1 * SEC_IN_MIN)

    if minutes < 10:
        minutes = f'0{minutes}'

    if seconds < 10:
        seconds = f'0{seconds}'    

    return f'{degrees}{DEGREE}{minutes}\'{seconds}\"'

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"