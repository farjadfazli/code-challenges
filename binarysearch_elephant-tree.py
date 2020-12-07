"""
Elephant Tree

Given a binary tree root, return the same tree except every node's value is replaced by its original value plus all of the sums of its left and right subtrees.

Constraints

    n ≤ 100,000 where n is the number of nodes in root

Example 1
Input
Visualize Tree

root = [2, [1, [0, null, null], null], [4, [3, null, null], null]]

Output
Visualize Tree

[10, [1, [0, null, null], null], [7, [3, null, null], null]]
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root == None:
            return
        print(root.val)
        self.solve(root.left)
        self.solve(root.right)
        if root.right is not None:
            root.val += root.right.val
        if root.left is not None:
            root.val += root.left.val
        return root