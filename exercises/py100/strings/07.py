"""
Is Empty or Blank?
Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. For example:

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
"""
def is_empty_or_blank(str):
    # return True if not str or str.isspace() else False
    # return str.strip(' ') == ''
    return not str.strip(' ')

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True