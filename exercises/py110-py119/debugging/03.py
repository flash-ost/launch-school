"""
Multiply List
You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.

def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])
"""
# With statement 'for item in lst:' we assign a value of list element to the local variable item.
# Inside loop body we reassign this local varible, but original element of the list remains the same.
# To fix this, we should reassign the list elements to new values.

def multiply_list(lst):
    ## Loop
    # for idx in range(len(lst)):
    #     lst[idx] *= 2

    # return lst

    ## Comprehension
    return [el * 2 for el in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])