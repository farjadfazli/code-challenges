"""
Parentheses Grouping

Given a string s containing balanced parentheses "(" and ")", split them into the maximum number of balanced groups.

Constraints

    n ≤ 100,000 where n is length of s.

Example 1

Input

s = "()()(()())"

Output

["()", "()", "(()())"]

"""
class Solution:
    def solve(self, s):
        result = []
        counter = 0
        openCount = 0
        closeCount = 0
        tempString = ""
        while counter < len(s):
            if s[counter] == "(":
                openCount += 1
                tempString += "("
            elif s[counter] == ")":
                closeCount += 1
                tempString += ")"
            if openCount == closeCount:
                result.append(tempString)
                tempString = ""
                openCount = 0
                closeCount = 0
            counter += 1
        return result