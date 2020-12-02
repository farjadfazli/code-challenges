"""
Univalue Tree

Given a binary tree root, return whether all values in the tree are the same.

Constraints

    n ≤ 100,000 where n is the number of nodes in root

Example 1
Input
Visualize Tree

root =

2

2

2

2

2
Output

True

Explanation

Every node has the value 2
Example 2
Input
Visualize Tree

root =

2

2

2

9
Output

False

Explanation

There is a node with a value 9 while others are 2
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, value=None):
        if root is None:
            return True
        if value is None:
            value = root.val
        print(root.val)
        return root.val == value and self.solve(root.right, value) and self.solve(root.left, value)