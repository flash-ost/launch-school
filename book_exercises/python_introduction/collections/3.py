# old_tuple = (1, 2, 3, 4, 5)
# new_tuple = tuple(reversed(old_tuple[1:len(old_tuple) - 1]))
# print(new_tuple)

old_tuple = (1, 2, 3, 4, 5)
new_tuple = old_tuple[3:0:-1]
print(new_tuple)

# reversing with slicing
print(old_tuple[4::-1])
print(old_tuple[-1::-1])
print(old_tuple[::-1])
print(old_tuple[-1:-6:-1])