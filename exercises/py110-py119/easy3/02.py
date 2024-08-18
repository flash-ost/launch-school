"""
After Midnight (Part 2)
As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

Examples
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

Disregard Daylight Savings and Standard Time and other irregularities.
"""

## Understanding
# Input: string with time in 24-hour format
# Output: int containing num of minutes based on input string
# first function: num of mins after midnight
# second function: num ofmins before midnight

## Test Cases
# Both 24:00 and 00:00 should return 0 in both functions

## Data structure
# No

## Algorithm
# Split the string (separator :), convert values to int
# After midnight: 
#  - convert hours to mins
#  - add from input 
# Before midnight:
#  - perform both actions of after midnight
#  - subtract result from num of mins in day (1440)
# Return result

MINS_IN_HOUR = 60
MINS_IN_DAY = 1440

def after_midnight(string):
    hours, minutes = [int(el) for el in string.split(':')]
    return (hours * MINS_IN_HOUR + minutes) % MINS_IN_DAY

def before_midnight(string):
    minutes = MINS_IN_DAY - after_midnight(string)
    return minutes % MINS_IN_DAY
    

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True