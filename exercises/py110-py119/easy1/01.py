"""
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

Example 1
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.
Example 2
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.
"""

## Problem

# Input: 6 numbers, one by one
# Output: message telling user whether last number was among previous 5

# Questions:
# - User can input any number or just integer?
# - Should we check the input for validity? And if so, what are criteria?

## Examples / Test Cases
# - message should be in format "num6 is / isn't in num1,num2,num3,num4,num5."
# - first 5 numbers are printed one after another, separated by commas without spaces

## Data Structures
# We will use a list to store numbers.

## Algorithm
# Create a list of numbers counter for prompt (5 first numbers): ['1st', '2nd' ...]
# Create an empty list for user's input
# Iterate over list:
#   - prompt user for input by asking for appropriate number (current list el)
#   - append input to list for input
# Prompt user for last number and save it in variable
# Use conditional statement to choose which message (is / isn't to print)
#   - print message with correct formatting

num_counter = ['1st', '2nd', '3rd', '4th', '5th']
user_input = []
for num in num_counter:
    user_input.append(input(f'Enter the {num} number: '))

last_num = input(f'Enter the last number: ')

verdict = 'is' if last_num in user_input else 'isn\'t'
print(f'{last_num} {verdict} in {','.join(user_input)}.')