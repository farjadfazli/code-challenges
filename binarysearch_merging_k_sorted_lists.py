"""
Merging K Sorted Lists

Given a list of sorted lists of integers, merge them into one large sorted list.

Can you do it better than O(kn log kn) where n is the length of the longest list, and k is the number of lists?
Example 1
Input

lists = [
    [],
    [],
    [10, 12],
    [],
    [3, 3, 13],
    [3],
    [10],
    [0, 7]
]

Output

[0, 3, 3, 3, 7, 10, 10, 12, 13]
"""
class Solution:
    def solve(self, lists):
        result = [num for list in lists for num in list]
        result.sort()
        return result