"""
Rotating Matrices
As we saw in the previous exercises, a matrix can be represented by a list of lists. For example, the 3x3 matrix shown below:

1  5  8
4  7  2
3  9  6
is represented by the following list of list:

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]
A 90-degree rotation of a matrix produces a new matrix in which each side of the matrix is rotated clockwise by 90 degrees. For example, the 90-degree rotation of the matrix shown above is:

3  4  1
9  7  5
6  2  8
A 90-degree rotation of a non-square matrix is similar. For example, given the following matrix:

3  4  1
9  7  5
its 90-degree rotation is:

9  3
7  4
5  1
Write a function that takes an arbitrary MxN matrix, rotates it clockwise by 90-degrees as described above, and returns the result as a new matrix. The function should not mutate the original matrix.

Examples
matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)
"""
## Understanding
# Input: list of lists representing a matrix
# Output: list of lists representing the original matrix rotated clockwise by 90 degrees

# Don't mutate original matrix

## Algorithm
# Create an empty list rotated for a new matrix
# Iterate over idxs in the first inner list of original matrix:
#   create empty list row
#   iterate over lists in original matrix in reverse order:
#       append idxth element of cirrent inner list to row
#   append row to rotated
# Return rotated

def rotate90(matrix):
    # rotated = []
    # for idx in range(len(matrix[0])):
    #     row = []
    #     for inner in matrix[::-1]:
    #         row.append(inner[idx])
    #     rotated.append(row)
    # return rotated     
    return [[inner[idx] for inner in matrix[::-1]] for idx in range(len(matrix[0]))]

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)
