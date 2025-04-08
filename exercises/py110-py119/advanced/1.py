"""
Transpose 3x3 Matrix
A 3x3 matrix can be represented by a list of nested lists: an outer list that contains three sub-lists that each contain three elements. For example, the 3x3 matrix shown below:

1  5  8
4  7  2
3  9  6
is represented by the following list of lists:

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]
A list of lists is sometimes called a nested list since each inner sub-list is nested inside an outer list. It also may be called a two-dimensional list.

To access an element in the matrix, you can use bracket notation twice (such as matrix[row][col]), and include both the row index and column index within the brackets. Given the above matrix, matrix[0][2] is 8, and matrix[2][1] is 9. An entire row in the matrix can be referenced using a single index: matrix[1] is the row (sub-list) [4, 7, 2]. Unfortunately, a convenient notation for accessing an entire column does not exist.

The transpose of a 3x3 matrix is the matrix that results from exchanging the rows and columns of the original matrix. For example, the transposition of the matrix shown above is:

1  4  3
5  7  9
8  2  6
Write a function that takes a list of lists that represents a 3x3 matrix and returns the transpose of the matrix. You should implement the function on your own, without using any external libraries.

Take care not to modify the original matrix -- your function must produce a new matrix and leave the input matrix list unchanged.

Examples
matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
"""
## Understanding
# Input: list if lists representing a matrix
# Output: list of lists representing a transposed matrix (columns become rows and vice versa)

# No external libraries
# Original matrix should not be mutated

## Algorithm
# Create an empty list new_matrix
# Iterate over indexes (idx) of first inner list in original matrix:
#   create empty list row
#   iterate over lists in original matrix:
#       append idxth element of current list to row
#   append row to new_matrix
# Return new_matrix

def transpose(matrix):
    # new_matrix = []
    # for idx in range(len(matrix[0])):
    #     row = []
    #     for inner in matrix:
    #         row.append(inner[idx])
    #     new_matrix.append(row)

    return [[inner[idx] for inner in matrix] for idx in range(len(matrix[0]))]

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True