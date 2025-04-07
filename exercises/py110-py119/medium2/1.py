"""
Lettercase Percentage Ratio
Write a function that takes a string and returns a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

Examples
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
"""

## Understanding
# Input: string
# Output: dictionary containing three properties
#   - percentage of lowercase letters in string
#   - percentage of uppercase letters in string
#   - percentage of chars that are neither

# Corresponding keys should be named lowercase/uppercase/neither
# Values should be numbers rounded to 2 decimal points and converted to string
# Input string will always contain at least one character

## Algorithm
# Create a dictionary with 3 properties as keys and 0s as values
# Iterate over chars in string:
#   If char is uppercase:
#       increment corresponding value in dict by 1
#   elif char is lowercase:
#       increment corresponding value in dict by 1
#   else (neither):
#       increment corresponding value in dict by 1
# Calculate the length of input string and store it in length variable
# Iterate over keys in dict:
#   divide corresponding value by string length
#   round result to 2 decimal places
#   convert result to string
#   split string with dot as separator
#   if length of second part is 1, add 0 char ot the end of the whole string
#   replace value in dict with string
# Return dict

def letter_percentages(string):
    results = { 'lowercase': 0,
                'uppercase': 0,
                'neither': 0, }
    
    for char in string:
        if char.isupper():
            results['uppercase'] += 1
        elif char.islower():
            results['lowercase'] += 1
        else:
            results['neither'] += 1

    length = len(string)
    for property in results:
        results[property] = f'{results[property] / length * 100:.2f}'

    return results           


expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)


