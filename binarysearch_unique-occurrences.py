"""
Unique Occurrences

Given a list of integers nums, return whether the number of occurrences of every value in the array is unique.

Note: Numbers can be negative.

Constraint

    n ≤ 100,000 where n is the length of nums

Example 1
Input

nums = [5, 3, 1, 8, 3, 1, 1, 8, 8, 8]

Output

True

Explanation

There's 1 occurrence of 5, 2 occurrences of 3, 3 occurrences of 1, and 4 occurrences of 8. All number of occurrences are unique.
Example 2
Input

nums = [-3, -1, -1, -1, -2, -2]

Output

True

Explanation

There's 1 occurrence of -3, 2 occurrences of -2, and 3 occurrences of -1. All number of occurrences are unique.
Example 3
Input

nums = [3, 1, 1, 2, 2, 2, 3]

Output

False

Explanation

There are 2 occurrences of 1, and 2 occurrences of 3. So the number of occurrences here is not unique.
"""
class Solution:
    def solve(self, nums):
        from collections import Counter
        result = Counter(nums)
        times = []
        for num in set(nums):
            times.append(result[num])
        return len(times) == len(set(times))