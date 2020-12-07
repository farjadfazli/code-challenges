"""
Central Linked List

Given a singly linked list node, return the value of the middle node. If there's two middle nodes, then return the second one.

Bonus: Solve using O(1)\mathcal{O}(1)O(1) space.

Constraints

    n ≤ 100,000 where n is the number of nodes in node

Example 1
Input

node = 0 → 1 → 2

Output

1
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        length = 0
        root = node
        while node:
            length += 1
            node = node.next
        length = length // 2
        length += 1
        while length > 1:
            root = root.next
            length -= 1
        return root.val