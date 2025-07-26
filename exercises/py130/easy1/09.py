"""
Basic Generator Function
Create a generator function that yields numbers from 1 to 5.
"""
def one_to_five():
    for num in range(1, 6):
        yield num

print(list(one_to_five()))