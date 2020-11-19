"""
Longest Common Prefix

Given a list of lowercase alphabet strings words, return the longest common prefix.
Example 1

Input

words = ["anthony", "ant", "antigravity"]

Output

"ant"

Explanation

"ant" is the longest common prefix between the three strings.
"""
class Solution:
    def solve(self, words):
        result = ""
        words.sort()
        print(words)
        for i in range(len(words[0])):
            if words[0][i] == words[-1][i]:
                result += words[0][i]
            else:
                break
        return result