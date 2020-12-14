"""
Detect Voter Fraud

Given a two dimensional list of integers votes, where each list has two elements [candidate_id, voter_id], report whether any voter has voted more than once.
Example 1

Input

votes = [
    [3, 1],
    [3, 0],
    [3, 4],
    [3, 3],
    [3, 2]
]

Output

False

Explanation

Every voter has voted once.
Example 2

Input

votes = [
    [2, 3],
    [2, 2],
    [2, 1],
    [2, 0],
    [2, 1]
]

Output

True

Explanation

The voter with voter_id 1 voted twice.
"""
class Solution:
    def solve(self, votes):
        # solution using dict:
        #
        # dict = {}
        # for vote in votes:
        #     if vote[1] in dict:
        #         dict[vote[1]] += 1
        #     else:
        #         dict[vote[1]] = 1
        # if 2 in dict.values():
        #     return True
        # else:
        #     return False
        
        # solution using list comprehension (faster!)
        
        result = [i[1] for i in votes]
        return len(result) != len(set(result))