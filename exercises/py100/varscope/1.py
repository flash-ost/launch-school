"""
What's my value? (Part 1)
What will the following code do and why? Don't run it until you have tried to answer.

if True:
    my_value = 20

print(my_value)
"""

# We will see the output 20.

if True:
    my_value = 20

print(my_value)

"""
What do you think will happen if we run the following code instead:

if False:
    my_new_value = 42

print(my_new_value)
"""
# Since the conditional expression is False, the block inside won't execute.
# Trying to use the undefined variable will lead to an error.

if False:
    my_new_value = 42

print(my_new_value)