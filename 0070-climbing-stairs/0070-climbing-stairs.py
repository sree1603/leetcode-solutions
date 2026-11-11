class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp = [-1]*(n+1)
        def climb(n):
            if n == 1 or n == 2:
                return n
            if dp[n]!= -1:
                return dp[n]
            dp[n] = climb(n-1)+climb(n-2)
            return dp[n]
        return climb(n)
        