"""
Greatest common divisors

Given a list of positive integers nums, return the largest positive integer that divides each of the integers.
Example 1

Input

nums = [6, 12, 9]

Output

3

Explanation

3 is the largest integer that divides into 6, 12, and 9.
Example 2

Input

nums = [6, 7, 9]

Output

1

Explanation

7 is a prime number so only 1 divides into it.
"""
class Solution:
    def solve(self, nums):
        if len(nums) == 1:
            return nums[0]
        import math
        smallest = min(nums)
        nums.remove(smallest)
        secondSmallest = min(nums)
        divisor = math.gcd(smallest, secondSmallest)
        biggest = max(nums)
        if biggest % divisor != 0:
            divisor = 1
        return divisor
