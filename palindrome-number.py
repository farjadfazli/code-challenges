"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

Input: x = -101
Output: false

Constraints:
    -231 <= x <= 231 - 1

Source: https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # we will determine if the integer is a palindrome by reversing it 
        # and seeing if reversed integer == integer
        if x < 0:
            return False
        reversed = 0
        current = x
        while current > 0:
            reversed *= 10
            calculation = current % 10
            reversed += calculation
            current = current // 10
        if reversed == x:
            return True
        return False
        
        # alternate solution by converting integer to string:
        # if str(x) == "".join(reversed(str(x))):
        #     return True
