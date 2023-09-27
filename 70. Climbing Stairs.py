#---- For a n steps stair, you can climb 1 or 2 steps at a time. Return the different options you can climb to the top
class solution(object):

    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
        def helper(self, n: int, memo: dict[int, int]) -> int:
            if n == 0 or n == 1:
                return 1
            if n not in memo:
                memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
            return memo[n]