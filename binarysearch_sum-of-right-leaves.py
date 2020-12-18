"""
Sum of Right Leaves

Given a binary tree root, return the sum of all leaves that are right children.

Constraints

    n ≤ 100,000 where n is the number of nodes in root

Example 1
Input
Visualize

root = [0, [4, null, null], [2, [1, [6, null, null], [3, null, null]], [7, null, null]]]

Output

10

Explanation

Since 7 + 3 = 10.
Example 2
Input
Visualize

root = [9, [3, [1, null, null], [2, null, null]], [8, [5, null, null], null]]

Output

2
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None:
            return 0
        if root.right is not None:
            if root.right.left is None and root.right.right is None:
                return root.right.val + self.solve(root.left)
        return self.solve(root.right) + self.solve(root.left)