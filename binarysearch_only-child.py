"""
Only Child

Given a binary tree root, return the number of nodes that are an only child. A node x is an only child if its parent has exactly one child (x).

Constraints

    n ≤ 100,000 where n is the number of nodes in root

Example 1
Input
Visualize

root = [0, [4, null, null], [2, [1, [3, null, null], null], null]]

Output

2

Explanation

Node 1 is an only child and 3 is an only child.
Example 2
Input
Visualize

root = [1, null, [3, [1, null, null], [1, null, null]]]

Output

1

Explanation

Node 3 is an only child
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # we have to count how many nodes have only one child (right or left)
        if root is None:
            return 0   
        onlyChildren = 0
        if (root.right == None and root.left != None) or (root.left == None and root.right != None):
            onlyChildren += 1
        onlyChildren += self.solve(root.right) + self.solve(root.left)
        return onlyChildren