"""
Pairwise Linked List Swap

Given a singly linked list node, swap each pair of nodes and return the new head.

Constraints

    n ≤ 100,000 where n is the number of nodes in node

Example 1
Input
Visualize

node = [0, 1, 3, 4]

Output
Visualize

[1, 0, 4, 3]

Example 2
Input
Visualize

node = [1, 2, 3]

Output
Visualize

[2, 1, 3]
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        current = node
        while current and current.next:
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next
        return node