"""
Reverse Sublists to Convert to Target

Given two lists of integers nums, and target, consider an operation where you take some sublist in nums and reverse it. Return whether it's possible to turn nums into target, given you can make any number of operations.
Example 1

Input

nums = [1, 2, 3, 8, 9]
target = [3, 2, 1, 9, 8]

Output

True

Explanation

We can reverse [1, 2, 3] and [8, 9]
Example 2

Input

nums = [10, 2, 3, 8, 9]
target = [3, 2, 1, 9, 8]

Output

False

"""
class Solution:
    def solve(self, nums, target):
        return sorted(nums) == sorted(target)