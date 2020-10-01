"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Source: https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if (x < 0):
            negative = True
        reversed = 0
        current = x
        if (negative):
            current *= -1        
        while current > 0:
            reversed *= 10
            calculation = current % 10
            reversed += calculation
            import math
            current = current // 10
        print(reversed)
        if (negative):
            reversed *= -1
        if (reversed > 2147483647 or reversed < -2147483648):
            return 0
        return reversed