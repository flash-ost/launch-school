"""
Problem 9
Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string. Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

Examples
print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
"""

# Input: 2 strings
# Output: number of times that second string occurs in the first string

# Second string will never be empty
# Occurences should not overlap

# Algorithm
# Initialize count to 0
# Initialize end to len(string2)
# While end <= len(string1):
#   if string1[end - len(string2):end] == string2:
#       count += 1
#       end += len(string2)
#   else:
#       end += 1
# Return count

# def count_substrings(str1, str2):
#     count = 0
#     end = len(str2)
#     while end <= len(str1):
#         if str1[end - len(str2):end] == str2:
#             count += 1
#             end += len(str2)
#         else:    
#             end += 1
#     return count       
def count_substrings(str1, str2):
    count = 0
    position = 0
    while position <= len(str1) - len(str2):
        idx = str1.find(str2, position)
        if idx == -1:
            break
        count += 1
        position = idx + len(str2)   
    return count    

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)