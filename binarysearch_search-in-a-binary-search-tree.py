"""
Search in a Binary Search Tree

Given a binary search tree root and an integer val, determine whether val is in the tree.

Constraints

    n ≤ 100,000 where n is the number of nodes in root

Example 1
Input
Visualize

root = [3, [2, null, null], [9, [7, [4, null, null], [8, null, null]], [12, null, null]]]

val = 4

Output

True

Example 2
Input
Visualize

root = [3, [2, null, null], [9, [7, [4, null, null], [8, null, null]], [12, null, null]]]

val = 100

Output

False
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, val):
        if root is None:
            return False
        if root.val == val:
            return True
        if root.val < val:
            return self.solve(root.right, val)
        if root.val > val:
            return self.solve(root.left, val)