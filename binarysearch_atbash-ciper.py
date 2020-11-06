"""
Atbash cipher

You are given a lowercase alphabet string text. Return a new string where every character in text is mapped to its reverse in the alphabet, so that a becomes z, b becomes y, c becomes x, and so on.
Example 1

Input

text = "abcdef"

Output

"zyxwvu"
"""
class Solution:
    def solve(self, text):
        import string
        alphabet = string.ascii_lowercase
        newString = ""
        for i in range(len(text)):
            indexOfLetter = alphabet.find(text[i])
            newString += alphabet[~indexOfLetter]
        return newString