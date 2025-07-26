"""
Display Info
Write a function display_info that takes a positional-only parameter data, and keyword-only parameters reverse and uppercase.

Example
print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC
"""
def display_info(data, /, *, reverse=False, uppercase=False):
    if reverse:
        data = data[::-1]
    if uppercase:
        data = data.upper()

    return data        

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC