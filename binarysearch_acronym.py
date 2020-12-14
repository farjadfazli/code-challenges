"""
Acronym

Given a string s representing a phrase, return its acronym. Acronyms should be capitalized and should not include the word "and".
Example 1

Input

s = "For your information"

Output

"FYI"

Example 2

Input

s = "National Aeronautics and Space Administration"

Output

"NASA"
"""
class Solution:
    def solve(self, s):
        output = ''
        words = s.split(' ')
        for word in words:
            if word == "and":
                continue
            output += word[0]
        return output.upper()

