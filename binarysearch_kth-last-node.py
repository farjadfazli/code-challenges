"""
Kth Last Node of a Linked List

Given a singly linked list node, return the value of the kth last node (0-indexed). k is guaranteed not to be larger than the size of the linked list.

This should be done in O(1)\mathcal{O}(1)O(1) space.

Constraints

    n ≤ 100,000 where n is the length of node

Example 1
Input

node = 1 → 2

k = 1

Output

1

Explanation

The second last node has the val of 1
Example 2
Input

node = 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9

k = 2

Output

7

Explanation

    Last node (index 0) has val of 9
    Second last node (index 1) has val of 8
    Third last node (index 2) has val of 7
"""
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        # tried to do two pointer method but ended up traversing twice...will come back to this!
        head = node
        stepsToMove = k
        slowPointer = head
        fastPointer = head
        length = 0
        while fastPointer.next is not None:
            length += 1
            stepsToMove -= 1
            fastPointer = fastPointer.next
        # once we have the length we can traverse length - k steps
        print(length)
        stepsToTraverse = length - k
        while stepsToTraverse > 0:
            slowPointer = slowPointer.next
            stepsToTraverse -= 1
        return slowPointer.val