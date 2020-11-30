"""
Word Machine

You are given a list of strings ops where each element is either:

    A non-negative integer that should be pushed into a stack
    "POP" meaning pop the top element in the stack
    "DUP" meaning duplicate the top element in the stack
    "+" meaning pop the top two and push the sum
    "-" meaning pop the top two and push top - second

Return the top element in the stack after applying all operations. If there are any invalid operations, return -1.

Constraints

    n ≤ 100,000 where n is the length of ops

Example 1
Input

ops = ["1", "5", "DUP", "3", "-"]
Output

-2
Explanation

Following the operations:

    We push 1 into the stack: [1]
    We push 5 into the stack: [1, 5]
    We duplicate the top element: [1, 5, 5]
    We push 3 into the stack: [1, 5, 5, 3]
    We pop 3 and 5 and push their difference 3 - 5: [1, 5, -2]

We return the top element which is -2
Example 2
Input

ops = ["+"]
Output

-1
Explanation

There's no elements in the stack so this is invalid.
"""
class Solution:
    def solve(self, ops):
        stack = []
        try:
            for i in ops:
                if i == "POP":
                    stack.pop()
                elif i == "DUP":
                    stack.append(stack[-1])
                elif i == "+":
                    stack.append(stack.pop() + stack.pop())
                elif i == "-":
                    stack.append(stack.pop() - stack.pop())
                elif i.isnumeric():
                    stack.append(int(i))
        except:
            return -1
        if len(stack) > 0:
            return stack[-1]
        return -1