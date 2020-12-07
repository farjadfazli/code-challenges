"""
Count BST Nodes in a Range

Given a binary search tree root, and integers lo and hi, return the count of all nodes in root whose values are between [lo, hi] (inclusive).

Constraints

    n ≤ 100,000 where n is the number of nodes in root

Example 1
Input
Visualize Tree

root = [3, [2, null, null], [9, [7, [4, null, null], [8, null, null]], [12, null, null]]]

lo = 5

hi = 10

Output

3

Explanation

Only 7, 8, 9 are between [5, 10].
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        if root is None:
            return 0
        if root.val >= lo and root.val <= hi:
            return 1 + self.solve(root.left, lo, hi) + self.solve(root.right, lo, hi)
        elif root.val < lo:
            return self.solve(root.right, lo, hi)
        else:
            return self.solve(root.left, lo, hi)