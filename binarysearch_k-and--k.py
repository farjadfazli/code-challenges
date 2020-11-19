"""
K and -K

Given a list of integers nums, return the largest integer k where k and -k both exist in nums (they can be the same integer). If there's no such integer, return -1.

Constraints

    n ≤ 100,000 where n is the length of nums

Example 1

Input

nums = [-4, 1, 8, -5, 4, -8]

Output

8

Example 2

Input

nums = [5, 6, 1, -2]

Output

-1

Example 3

Input

nums = [1, 2, 0, 3, 4]

Output

0
"""
class Solution:
    def solve(self, nums):
        if 0 in nums:
            return 0
        nums.sort()
        numSet = set([x for x in nums if x>0])
        for i in nums:
            if i*-1 in numSet:
                return i*-1
        return -1