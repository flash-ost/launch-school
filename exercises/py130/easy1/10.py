"""
Generator with User Input
Create a generator function that yields user input strings until the word "stop" is entered.
"""
def input_yielder():
    while True:
        value = input()
        if value == 'stop':
            break
        yield value   

print(list(input_yielder()))