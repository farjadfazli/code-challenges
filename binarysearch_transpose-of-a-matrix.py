"""
Transpose of a Matrix

Given an integer square (n by n) matrix, return its transpose. A transpose of a matrix switches the row and column indices. That is, for every r and c, matrix[r][c] = matrix[c][r].

For example, given matrix

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

it becomes

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

Constraints

    n ≤ 100

Example 1

Input

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output

[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

"""
class Solution:
    def solve(self, matrix):
        # we will take the nth element of each sublist and put it in the nth sublist of the new matrix
        result = []
        length = len(matrix)
        counter = 0
        while counter < length:
            for row in matrix:
                result.append(row[counter])
            counter += 1
        i = 0
        final = []
        while i < len(result):
            final.append(result[i:i+length])
            i+=length
        return final