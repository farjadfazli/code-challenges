"""
Inorder Traversal

Given a binary tree root, return an inorder traversal of root as a list.

Bonus: Can you do this iteratively?

Constraints

    n ≤ 100,000 where n is the number of nodes in root

Example 1
Input
Visualize

root = [1, null, [159, [80, null, null], null]]

Output

[1, 80, 159]
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        result = []
        if root is not None:
            result = self.solve(root.left)
            result.append(root.val)
            result += self.solve(root.right)
        return result