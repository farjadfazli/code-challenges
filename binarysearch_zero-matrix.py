"""
Zero Matrix

Given a two-dimensional matrix of integers, for each zero in the original matrix, replace all values in its row and column with zero, and return the resulting matrix.

Constraints

    n, m ≤ 250 where n and m are the number of rows and columns in matrix

Example 1
Input

matrix = [
    [5, 0, 0, 5, 8],
    [9, 8, 10, 3, 9],
    [0, 7, 2, 3, 1],
    [8, 0, 6, 7, 2],
    [4, 1, 8, 5, 10]
]

Output

[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 3, 9],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 5, 10]
]

Explanation

These rows contain a 0: [0, 2, 3] and the returned matrix contains 0 in those rows.
These columns contain a 0: [0, 1, 2] and the returned matrix contains 0 in those columns.
"""
class Solution:
    def solve(self, matrix):
        # keep track of rows and columns that contain 0's
        rows = set()
        columns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        # iterate through matrix again and set values to 0 if the row or column it is in contained a 0 as per above
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in columns:
                    matrix[i][j] = 0
        return matrix