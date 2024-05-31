def caps_long(string):
    return string.upper() if len(string) > 10 else string

print(caps_long('hello world'))
print(caps_long('goodbye'))