"""
Largest Gap

Given a list of integers nums, return the largest difference of two consecutive integers in the sorted version of nums.

Constraints

    n ≤ 100,000 where n is the length of nums

Example 1

Input

nums = [4, 1, 2, 8, 9, 10]

Output

4

Explanation

The largest gap is between 4 and 8.
"""
class Solution:
    def solve(self, nums):
        largestDifference = 0
        sortedNums = sorted(nums)
        for i in range(len(sortedNums) - 1):
            currentDifference = sortedNums[i+1] - sortedNums[i]
            if currentDifference > largestDifference:
                largestDifference = currentDifference
        return largestDifference
        
        # alternate solution:
        # return max([sortedNums[i+1] - sortedNums[i] for i in range(len(sortedNums) - 1)])