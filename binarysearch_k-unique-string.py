"""
K Unique String

Given a string s of lowercase alphabet characters, and an integer k, return the minimum number of changes needed in the string (one change involves changing a single character to any other character) so that the resulting string has at most k distinct characters.

Constraints

    n ≤ 10,000 where n is the length of s
    1 ≤ k ≤ 26

Example 1
Input

s = "daabbccaa"

k = 3

Output

1

Explanation

We can remove the "d" to get 3 distinct characters (a, b, and c).
Example 2
Input

s = "daabbccaad"

k = 3

Output

2

Explanation

We must remove either 2 "b"s, 2 "c"s, or 2 "d"s.
"""
class Solution:
    def solve(self, s, k):
        from collections import Counter
        # get a count of the number of distinct letters and the occurrences of each letter
        count = Counter(s)
        # if there are <= k distinct letters, we don't need to do anything, so return 0
        if len(count) <= k:
            return 0
        # we need the difference between k and len(count) to determine how many letters we will have to change
        diff = len(count) - k
        # once we know how many letters we have to change, we can get a sum of how many times the least occurring letters appear
        # this can definitely be more optimized...
        listOfLetters = list(reversed(sorted(list(count.values()))))
        return sum(listOfLetters[-diff:])