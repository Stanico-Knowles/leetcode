"""
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer 
    range [-231, 231 - 1], then return 0

    Example 1:

        Input: x = 123
        Output: 321

    Example 2:

        Input: x = -123
        Output: -321

    Example 3:

        Input: x = 120
        Output: 21
"""

import sys

class Solution:
    def reverse(self, x: int) -> int:
        x_to_string = str(abs(x))
        reversed_string = x_to_string[::-1]
        reversed_int = int(reversed_string) if x >= 0 else -abs(int(reversed_string)) 
        if reversed_int > 2**31 or reversed_int < -2**31 - 1:
            return 0
        return reversed_int 

print(2147483648 < 9646324351)
print(Solution().reverse(1534236469))