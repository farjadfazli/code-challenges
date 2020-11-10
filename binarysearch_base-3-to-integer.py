"""
Base 3 to integer

Given a string s representing a number in base 3 (consisting only of 0, 1, or 2), return its decimal integer equivalent.
Example 1

Input

s = "10"

Output

3

Example 2

Input

s = "21"

Output

7

"""
class Solution:
    def solve(self, s):
        # we can use python's built in int() function and specify the base
        return int(s, 3)