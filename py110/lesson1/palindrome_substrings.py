"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

def substrings(string):
    substrings = []
    for index in range(len(string) - 1):
        substring = string[index]
        for inner_index in range(index + 1, len(string)):
            substring += string[inner_index]
            substrings.append(substring)

    return substrings       


def is_palindrome(string):
    return string == string[::-1]

def palindrome_substrings(string):
    result = []
    substrings_list = substrings(string)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)

    return result


# Test cases:

# Comments show expected return values
print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))    # ['repaper', 'epape', 'pap']
print(palindrome_substrings("supercalifragilisticexpialidocious")) # ["ili"]