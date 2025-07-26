"""
Reverse String
Use a generator expression to yield each character of a string in reverse order.
"""
string = 'hello'
gen = (char for char in string[::-1])
print(list(gen))