"""
Rotate by 90 Degrees Counter-Clockwise

Given a two-dimensional square matrix, rotate it 90 degrees counter-clockwise.
Example 1
Input

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output

[
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7]
]
"""
class Solution:
    def solve(self, matrix):
        # first we zip the matrix in order to combine every ith element of each list
        zipped = zip(*matrix)
        # then we can reverse this to obtain the desired rotation
        return (list((reversed(list(zipped)))))