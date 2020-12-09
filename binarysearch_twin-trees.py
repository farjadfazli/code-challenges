"""
Twin Trees

Given two binary trees, root0 and root1, return whether their structure and values are equal.

Constraints

    n ≤ 100,000 where n is the number of nodes in root0
    m ≤ 100,000 where m is the number of nodes in root1

Example 1
Input
Visualize Tree

root0 = [0, [5, null, null], [9, null, null]]

root1 = [0, [5, null, null], [9, null, null]]

Output

True

Explanation

These two trees have the same values and same structure.
Example 2
Input
Visualize Tree

root0 = [0, [5, null, null], [9, null, null]]

root1 = [1, [2, null, null], [2, null, null]]

Output

False

Explanation

These two trees are not twins since their values are different.
Example 3
Input
Visualize Tree

root0 = [0, [5, null, null], null]

root1 = [0, null, [5, null, null]]

Output

False

Explanation

These two trees are not twins since their structure is different.

"""

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root0, root1):
        if root0 is None and root1 is None:
            return True
        if root0 is None or root1 is None:
            return False
        return (root0 and root1) and (root0.val == root1.val) and self.solve(root0.right, root1.right) and self.solve(root0.left, root1.left)