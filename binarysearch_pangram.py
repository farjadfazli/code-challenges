"""
Pangram

Given a string s, representing a sentence, return whether every letter (case-insensitive) of the alphabet is used at least once.
Example 1

Input

s = "A quick brown fox jumps over the lazy dog"

Output

True

Example 2

Input

s = "The jay, pig, fox, tiger and my wolves quack!"

Output

False

Explanation

This sentence is missing a "z"
"""
class Solution:
    def solve(self, s):
        import string
        alphabet = list(string.ascii_lowercase)
        for x in s:
            if x.lower() in alphabet:
                alphabet.remove(x.lower())
        return len(alphabet) == 0