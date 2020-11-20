"""
Longest Interval Containing One Number

You are given a list of unique integers nums. Return the size of the largest inclusive interval [start, end] such that it contains exactly one number in nums.

Constraints

    1 ≤ n ≤ 100,000 where n is the length of nums
    1 ≤ start ≤ end ≤ 100,000

Example 1

Input

nums = [10, 5, 19]

Output

99990

Explanation

The largest interval that contains one number is [11, 100000] which contains 19.
Example 2

Input

nums = [5, 50000, 90000]

Output

89994

Explanation

The largest interval that contains one number is [6, 89999] which contains 50,000.
"""
class Solution:
    def solve(self, nums):
        # we will sort the list and compare two numbers with one in between them
        nums.append(0)
        nums.append(100001)
        nums.sort()
        interval = 0
        for i in range(len(nums) - 2):
            if (nums[i+2]) - (nums[i]) > interval:
                interval = (nums[i+2]) - (nums[i])
        return interval-1