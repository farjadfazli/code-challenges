"""
Z Sum

Given an n by n integer matrix, return the sum of all elements that form a Z in the matrix. For example, given:

1 2 3
4 5 6
7 8 9

The Z that's formed is [1, 2, 3, 5, 7, 8, 9] and its sum is 35.

Constraints

    n ≤ 1000

Example 1

Input

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output

35
"""
class Solution:
    def solve(self, matrix):
        if len(matrix) == 1:
            return sum(matrix[0])
        if len(matrix) == 0:
            return 0
            
        # to find the biggest Z we first have to add all the elements in the first and last rows
        firstRow = sum(matrix[0])
        lastRow = sum(matrix[len(matrix)-1])
        
        # then we will add elements along the diagonal
        n = len(matrix) - 1
        diagonal = 0
        pointer = n - 1
        for i in matrix[1:n]:
            diagonal += i[pointer]
            pointer -= 1
            
        return firstRow + lastRow + diagonal