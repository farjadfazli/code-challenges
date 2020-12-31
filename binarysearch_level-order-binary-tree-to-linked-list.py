"""
Level Order Binary Tree to Linked List

Given a binary tree root, convert it to a singly linked list using level order traversal.

Constraints

    1 ≤ n ≤ 100,000 where n is the number of nodes in root

Example 1
Input
Visualize

root = [1, [2, null, null], [3, [4, null, null], [5, null, null]]]

Output
Visualize

[1, 2, 3, 4, 5]

Example 2
Input
Visualize

root = [1, [0, null, null], [2, null, null]]

Output
Visualize

[1, 0, 2]
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, root):
        # we have to traverse the binary tree and add node values to a linked list
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        values = [value for sublist in result for value in sublist]
        head = LLNode(values[0])
        main = head
        for num in values[1:]:
            head.next = LLNode(num)
            head = head.next
        return main