from math import log
"""
This solution is from leetcode, mine had an error with log3(243) beeing 4.99999 when it is actually 5, so the problem didn't pass the tests.
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        # Since error exist, can't use float.is_integer() to check
        # So I choose to check it back
        if n <= 0: return False
        res = round(log(n, 3))
        return 3**res == n
            