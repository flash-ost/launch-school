"""
Staggered Case (Part 1)
Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between upper and lower case.

Examples
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
"""

## Understanding
# Input: string
# Output: modified input string. Every other character starting from the first should be capitalized
#   and followed by lowercase or non-alphabetic char. Non-alphabetic chars count for capitalization order, just like alphabetic:
#   'b_B' -> 'B_B'
# Implicit rules: empty input string = empty output string

## Algorithm
# Initialize new_string to empty string
# Initialize uppercase switch to True
# Iterate over chars input string:
#   If switch equeals True:
#       convert char to upper case and append to new_string
#   else:
#       append char to new_string
#   toggle switch
# Return new_string

def staggered_case(string):
    new_string = ''
    uppercase = True
    for char in string:
        new_string += char.upper() if uppercase else char.lower()
        uppercase = not uppercase
    return new_string

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
