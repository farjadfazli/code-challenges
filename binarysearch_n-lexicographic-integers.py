"""
N Lexicographic Integers

Given an integer n, return first n integers sorted in lexicographic order.
Example 1
Input

n = 12

Output

[1, 10, 11, 12, 2, 3, 4, 5, 6, 7, 8, 9]

Lexicographic order

To determine which comes first in lexicographic order, compare the first digit of both numbers to see which is smaller, and if they match, compare the second digit, and so on. If they are all the same and one number has fewer digits, then it comes first.

For example, [1, 10, 2, 21, 3] is in lexicographic order.

"""
class Solution:
    def solve(self, n):
        result = []
        for i in range(1,n+1):
            result.append(str(i))
        result = sorted(result)
        return [int(x) for x in result]