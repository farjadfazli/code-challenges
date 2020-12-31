"""
Palindrome Linked List

Given a singly linked list node whose values are integers, determine whether the linked list forms a palindrome.

Constraints

    n ≤ 100,000 where n is the length of node

Example 1
Input
Visualize

node = [5, 3, 5]

Output

True

Explanation

5 -> 3 -> 5 is a palindrome.
Example 2
Input
Visualize

node = [12, 8, 12]

Output

True

Explanation

The values of the linked list are the same forwards and backwards.
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if node == None:
            return True
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return values == list(reversed(values))