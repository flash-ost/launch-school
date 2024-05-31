my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# new_list = [ 'even' if number % 2 == 0 else 'odd'
#              for number in my_list ]

# OR

# def even_or_odd(number):
#     return 'even' if number % 2 == 0 else 'odd'

# new_list = [ even_or_odd(number)
#              for number in my_list ]


new_list = []
for num in my_list:
    if num % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

print(new_list)        