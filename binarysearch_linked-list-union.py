"""
Linked List Union

Given two sorted linked lists node0, and node, return a new sorted linked list containing the union of the two lists.
Example 1
Input
Visualize

ll0 = [1, 3, 4]

ll1 = [2, 3, 4]

Output
Visualize

[1, 2, 3, 4]
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, ll0, ll1):
        # traverse both lists and compare the nodes at each position
        newNode = LLNode(0)
        head = newNode
        while ll0 and ll1:
            if ll0.val == ll1.val:
                head.next = LLNode(ll0.val)
                ll0 = ll0.next
                ll1 = ll1.next
            elif ll0.val < ll1.val:
                head.next = LLNode(ll0.val)
                ll0 = ll0.next
            else:
                head.next = LLNode(ll1.val)
                ll1 = ll1.next
            head = head.next
        head.next = ll0 or ll1
        return newNode.next