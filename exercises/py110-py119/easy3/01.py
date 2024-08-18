"""
After Midnight (Part 1)
The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

You may not use Python's datetime module.

Examples
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
"""

## Understanding
# Input: integer representing time in minutes
# Output: time in 24-hour format ('hh:mm'), converted from minutes
# Explicit rules:
#   - if integer is positive, count onwards (100 = 01:40)
#   - if integer is negative, count backwards (-100 = 22:20)
#   - function should work with any integer input
#   using datetime module is prohibited

## Test Cases
# No new info

## Data structure
# No

## Algorithm
# Get remainder of dividing input by num of mins in a day (remove excess minutes)
# Convert result to hours and minutes
# Format output for hours and mins (if < 10, add leading 0)
# Return formatted string

MINS_IN_DAY = 1440
MINS_IN_HOUR = 60

def time_of_day(mins):
    hours_mins = divmod(mins % MINS_IN_DAY, MINS_IN_HOUR)
    return f'{hours_mins[0]:02d}:{hours_mins[1]:02d}'    

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True