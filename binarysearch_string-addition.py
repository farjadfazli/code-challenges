"""
String Addition

Given two strings a, and b, both representing an integer, add them and return it in the same string representation.

Bonus: can you implement the addition directly, instead of using eval or built-in big integers?

Constraints`

    n ≤ 200 where n is the length of a
    m ≤ 200 where m is the length of b

Example 1

Input

a = "12"
b = "23"

Output

"35"

Explanation

12 + 23 = 35
"""
class Solution:
    def solve(self, a, b):
        return str(int(a)+int(b))