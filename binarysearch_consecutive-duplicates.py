"""
Consecutive Duplicates

Given a string s, consisting of "X" and "Y"s, delete the minimum number of characters such that there's no consecutive "X" and no consecutive "Y".

Constraints

    n ≤ 100,000 where n is the length of s

Example 1

Input

s = "YYYXYXX"

Output

"YXYX"

Explanation

One solution is to delete the first two "Y"s and the last "X".
"""
class Solution:
    def solve(self, s):
        i = 0
        indicesToRemove = []
        while i < len(s)-1:
            if s[i] == s[i+1]:
                indicesToRemove.append(i)
                i += 1
                continue
            i += 1
        new_str = ''.join([s[i] for i in range(len(s)) if i not in indicesToRemove])
        return new_str