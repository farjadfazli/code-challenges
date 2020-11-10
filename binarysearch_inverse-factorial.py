"""
Inverse Factorial

The factorial of a number n is defined as n! = n * (n - 1) * (n - 2) * ... * 1.

Given a positive integer a, return n such that n! = a. If there is no integer n that is a factorial, then return -1.

Constraints

    n < 2 ** 31

Example 1

Input

a = 6

Output

3

Explanation

3! = 6
Example 2

Input

a = 10

Output

-1

Explanation

10 is not any integer factorial.
"""
class Solution:
    def solve(self, a):
        # divide a by consecutive integers
        i = 2
        while a > 1:
            a /= i
            i += 1
            # if a is no longer an integer then it can't be an inverse factorial
            if a.is_integer() == False:
                return -1
        # return the last number we divided by
        return i - 1