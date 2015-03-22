class Solution:
    # @return an integer
    def numTrees(self, n):

        dp = [1, 1, 2]

        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n-2)]

            for i in range(3, n+1):
                for j in range(0,i):
                    dp[i] += dp[j]*dp[i-j-1]
            return dp[n]
