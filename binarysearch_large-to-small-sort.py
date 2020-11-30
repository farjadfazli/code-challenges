"""
Large to Small Sort

Given a list of integers nums, sort the list in the following way:

    First number is the maximum
    Second number is the minimum
    Third number is the 2nd maximum
    Fourth number is the 2nd minimum
    And so on.

Constraints

    n ≤ 100,000 where n is the length of nums.

Example 1

Input

nums = [5, 2, 9, 3]

Output

[9, 2, 5, 3]

Example 2

Input

nums = [1, 9, 9]

Output

[9, 1, 9]
"""
class Solution:
    def solve(self, nums):
        largestFirst = sorted(nums, reverse=True)
        smallestFirst = sorted(nums)
        result = []
        for i in range(len(largestFirst)//2):
            result.append(largestFirst[i])
            result.append(smallestFirst[i])
        if len(nums) % 2 == 1:
            result.append(largestFirst[len(largestFirst)//2])
        return result