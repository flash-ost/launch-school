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

## Understanding the Problem
# Input:
#   - number of available blocks
# Output:
#   - number of leftover blocks

# Explicit rules:
#   - layered structure
#   - top layer consists of single block
#   - 4 blocks in lower layer per 1 in upper layer

# Implicit rules:
#   - The number of blocks in a layer is layer number * layer number.

# Questions:
# - What is meant by gaps between blocks?

## Examples and test cases
# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True   1 - 1 = 0
# print(calculate_leftover_blocks(2) == 1)  # True   2 - 1 = 1
# print(calculate_leftover_blocks(4) == 3)  # True   4 - 1 = 3
# print(calculate_leftover_blocks(5) == 0)  # True   5 - (1 + 4) = 0
# print(calculate_leftover_blocks(6) == 1)  # True   6 - (1 + 4) = 1
# print(calculate_leftover_blocks(14) == 0) # True   14 - (1 + 4 + 9) = 0

## Data Structures
# We don't really need a complex data structure.
# Several integers will be sufficient.

## Algorithm
# - Initialize var with remaining blocks to passed value
# - Check whether there are any blocks
# - If not, return 0. Else:
# - Create a var with layer count (first = 1)
# - Create a var with num of blocks needed for current layer
# - While there are enough blocks to biuld a new layer:
#   - update num of available blocks (build a layer)
#   - update layer count
#   - calculate num of blocks needed for a new layer
# - Return number of leftover blocks

def calculate_leftover_blocks(blocks_remaining):
    if blocks_remaining:
        layer_num = 1
        layer_blocks = 1
        while blocks_remaining >= layer_blocks:
            blocks_remaining -= layer_blocks
            layer_num += 1
            layer_blocks = layer_num ** 2
    return blocks_remaining

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True  