"""
Recursive Index

Given a list of integers nums and an integer k, let's create a new set of possible elements { nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } stopping before it's out of index.

Return the size of this set, or -1 if there's a cycle.
Example 1

Input

nums = [1, 2, 3, 4, 5]
k = 0

Output

5

Explanation

We visit indices {0, 1, 2, 3, 4}

    A[0] which has value of 1
    A[1] which has value of 2
    A[2] which has value of 3
    A[3] which has value of 4
    A[4] has value of 5 and A[5] is out of index.

Example 2

Input

nums = [4, 2, 1, 1, 1]
k = 3

Output

-1

Explanation

We visit indices {3, 1, 2, 1, ...} which has a cycle
"""
class Solution:
    def solve(self, nums, k):
        result = []
        while k < len(nums):
            result.append(nums[k])
            k = nums[k]
            if len(result) > len(nums):
                return -1
        return len(result)