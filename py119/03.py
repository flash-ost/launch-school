"""
Problem 3
Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase. Other characters should remain the same.

Examples
original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
"""

# Input: string
# Output: copy of input string with every second character in every third word converted to uppercase

# Other characters should remain the same

## Algorithm
# Split string into a list of words
# Iterate over idx in range from 2 to length of list and step 3
#   convert word under idx to list of chars
#   iterate over idx2 in range from 1 to length of list of chars and step 2
#       reassign element under idx2 to its uppercase variant
#   join list of chars back to string
#   reassign string under idx with a new string
# join words back to string
# return new string

def to_weird_case(string):
    words = string.split()
    for i in range(2, len(words), 3):
        chars = list(words[i])
        for j in range(1, len(chars), 2):
            chars[j] = chars[j].upper()
        words[i] = ''.join(chars) 
    return ' '.join(words)            

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)