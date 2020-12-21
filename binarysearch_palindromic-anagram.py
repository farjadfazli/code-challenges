"""
Palindromic Anagram

Given a string s, determine whether any anagram of s is a palindrome.

Constraints

    n ≤ 100,000 where n is the length of s

Example 1
Input

s = "carrace"

Output

True

Explanation

"carrace" should return true, since it can be rearranged to form "racecar", which is a palindrome.
"""
class Solution:
    def solve(self, s):
        from collections import Counter
        count = Counter(s)
        oddNums = 0
        for x in count.values():
            # check if count of odd values is exactly 1
            if x % 2 == 1:
                if oddNums == 0:
                    oddNums += 1
                    continue
                # if we have more than one odd value, return False
                return False
        return True