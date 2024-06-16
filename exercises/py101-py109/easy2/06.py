"""
The End Is Near But Not Here
Write a function that returns the next to last word in the string argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two words.

Examples
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
"""
def penultimate(string):
    return string.split()[-2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

def middle(string):
    words = string.split()
    return words[(len(words) // 2)]

print(middle('a b'))
print(middle('a b c'))
print(middle('a b c d'))