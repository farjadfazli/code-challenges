"""
Home Run

Given a non-negative integer n, return the length of the longest consecutive run of 1s in its binary representation.
Example 1
Input

n = 156

Output

3

Explanation

156 is10011100 in binary and there's a run of length 3.
"""
class Solution:
    def solve(self, n):
        if n == 0:
            return 0
        binary = bin(n)
        counter = 1
        maxCounter = 1
        for i in range(len(binary) - 1):
            if binary[i] == "1" and binary[i+1] == "1":
                counter += 1
                maxCounter = max(counter, maxCounter)
            else:
                counter = 1
        return maxCounter