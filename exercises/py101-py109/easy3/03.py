"""
Bannerizer
Write a function that takes a short line of text and prints it within a box.

Example 1Copy Code
print_in_box('To boldly go where no one has gone before.')
Output for Example 1
+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+
Example 1
print_in_box('')
Output for Example 2
+--+
|  |
|  |
|  |
+--+
You may assume the output will always fit in your terminal window.
"""
def print_in_box(string):
    outer_string = f'+-{'-' * len(string)}-+'
    empty_string = f'| {' ' * len(string)} |'

    print(outer_string)
    print(empty_string)
    print(f'| {string} |')
    print(empty_string)
    print(outer_string)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')    