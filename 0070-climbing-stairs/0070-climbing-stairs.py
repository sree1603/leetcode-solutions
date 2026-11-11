class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        dp[1] = 1
        dp[2] = 2
        def climb(n):
            if n == 1 or n == 2:
                return n
            if n in dp:
                return dp[n]
            dp[n] = climb(n-1)+climb(n-2)
            return dp[n]
        return climb(n)
        