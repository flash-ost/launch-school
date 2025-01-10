"""
Leftover Blocks
You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

The building blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between blocks.
Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.
"""

## Understanding
# Input: integer - number of available blocks
# Output: integer - number of leftover blocks after building the highest possible structure

# Explicit rules
# - building blocks are cubes
# - top layer is a single block
# - block in upper layer must be supported by four blocks in a lower layer
# - block in lower layer can support more than one block in upper layer
# - no gaps between blocks allowed

# Implicit rules
# - number of blocks in layer correlates with that layer number
# - number of blocks in layer: layer number squared

# Clarifying questions
# - How are upper blocks placed on the lower ones?

## Data Structure
# Just integer to store the number of blocks left after adding layers

## Algorithm
# Initialize available_blocks variable to number of blocks provided as input
# Initialize layer_number variable to 1
# While available_blocks > 0:
#   calculate num of blocks needed for current layer
#   if there are enough blocks blocks to build it:     
#       subtract num of blocks needed for this layer from num of available blocks
#       increment layer_number by 1
#   else:
#       return available_blocks

# def calculate_leftover_blocks(blocks_remaining):
#     if blocks_remaining:
#         layer_num = 1
#         layer_blocks = 1
#         while blocks_remaining >= layer_blocks:
#             blocks_remaining -= layer_blocks
#             layer_num += 1
#             layer_blocks = layer_num ** 2
#     return blocks_remaining

def calculate_leftover_blocks(blocks):
    available_blocks = blocks
    layer_number = 1
    layer_blocks = layer_number

    while available_blocks >= layer_blocks:
        available_blocks -= layer_blocks
        layer_number += 1
        layer_blocks = layer_number ** 2
    return available_blocks   

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True  