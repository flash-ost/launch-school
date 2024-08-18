"""
Name Swapping
Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.

Example
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").
"""

## Understanding
# Input: string consisting of a first name, a space, and a last name
# Output: string consisting of the last name, a comma, a space, and the first name
# Explicit rules
# Input string won't include middle names, initials, or suffixes ("Jr.", "Sr.")

## Test Cases
# No new info

## Data Structure
# No

## Algorithm
# Split original string
# Create new formatted string and return

# # First solution
# def swap_name(name):
#     first, last = name.split()
#     return f'{last}, {first}'

# # Second solution
# def swap_name(name):
#     return ', '.join(name.split()[::-1])

# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

"""
Further Exploration
Suppose the named person has one or more middle names? Refactor the current solution so it can accommodate this. The middle names should be listed after the first name:

print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
"""

def swap_name(name):
    split_names = name.split()
    return f'{split_names[-1]}, {' '.join(split_names[:-1])}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True