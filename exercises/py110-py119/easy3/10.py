"""
Matching Parenthesis?
Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

Examples
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
Note that balanced pairs must start with a (, not a ).
"""

## Understanding
# Input: string
# Output: boolean - True if all parentheses in the string are properly balanced, False otherwise
# Explicit rules
# To be properly balanced, parentheses must occur in matching '(' and ')' pairs.
# Balanced pairs must start with a (, not a ).

## Test Cases
# Strings with no parentheses are considered balanced.

## Data Structure
# No

## Algorithm
# Initialize counter to 0
# Iterate over chars in string:
#   if counter is less than -1:
#       return False
#   if char == '('
#       increment counter by 1
#   elif char == ')'
#       decrement counter by 1
# Return True if counter == 0, False otherwise

# def is_balanced(string):
#     counter = 0
#     for char in string:
#         if counter == -1:
#             return False
#         if char == '(':
#             counter += 1
#         elif char == ')':
#             counter -= 1
#     return counter == 0          

# print(is_balanced("What (is) this?") == True)        # True
# print(is_balanced("What is) this?") == False)        # True
# print(is_balanced("What (is this?") == False)        # True
# print(is_balanced("((What) (is this))?") == True)    # True
# print(is_balanced("((What)) (is this))?") == False)  # True
# print(is_balanced("Hey!") == True)                   # True
# print(is_balanced(")Hey!(") == False)                # True
# print(is_balanced("What ((is))) up(") == False)      # True


"""
Further Exploration
There are a few other characters that should be matching as well. Square brackets and curly brackets normally come in pairs. Quotation marks(single and double) also typically come in pairs and should be balanced. Can you expand this function to take into account those characters?
"""

def is_balanced(string):
    # Handle brackets
    closing = {'}': '{', ')': '(', ']': '['}
    stack = []

    for char in string:
        if char in closing.values():
            stack.append(char)
        elif char in closing.keys():
            if closing[char] in stack:
                stack.remove(closing[char])
            else:
                return False
            
    # Handle quotes and double quotes
    if string.count("'") % 2 == 1 or string.count('"') % 2 == 1:
        return False
    
    return not stack   

print(is_balanced("What [is] this?") == True)
print(is_balanced("What is} this?") == False)
print(is_balanced("What {is this?") == False)
print(is_balanced("({What} (is this))?") == True)
print(is_balanced("((What)) (is this))?") == False)
print(is_balanced("Hey!") == True)
print(is_balanced(")Hey!(") == False)
print(is_balanced("What ({is]}) up(") == False)   
print(is_balanced("{What }is{{{}}} this?}") == False) # True
print(is_balanced("What [is]]] this?") == False)    # True
print(is_balanced("What {is} this?") == True)        # True
print(is_balanced("What is] this?") == False)        # True
print(is_balanced("What [is this?") == False)        # True
print(is_balanced("[{What} [is this]]?") == True)    # True
print(is_balanced("[[What]] {is this}}?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced("]Hey![") == False)                # True
print(is_balanced("What ({is})) up(") == False)      # True   
