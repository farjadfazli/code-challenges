"""
Odd number of digits

Given a list of positive integers nums, return the number of integers that have odd number of digits.
Example 1

Input

nums = [1, 800, 2, 10, 3]

Output

4

Explanation

[1, 800, 2, 3] have odd number of digits.
"""
class Solution:
    def solve(self, nums):
        result = 0
        for num in nums:
            if len(str(num)) % 2:
                result += 1
        return result