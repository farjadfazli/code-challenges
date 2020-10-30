"""
High frequency

Given a list of integers nums, find the most frequently occurring element and return the number of occurrences of that element.

For example, given the list [1, 4, 1, 7, 1, 7, 1, 1], return 5 since the the element 1 appears 5 times.

Constraints

    n ≤ 100,000 where n is the length of nums
"""
class Solution:
    def solve(self, nums):
        # we want to return the number of times that the most frequently occurring elements appears in the list
        
        # maxCount = 0
        # for x in nums:
        #     if nums.count(x) > maxCount:
        #         maxCount = nums.count(x)
        # return maxCount
        
        # more efficient implementation with dict:
        
        dict = {}
        
        for x in nums:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        return max(dict.values())