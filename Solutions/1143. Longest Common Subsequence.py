class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        # dynamic programming
        # bottom right to top left (bottom up approach)
        # if they are the same characters then cell = diagonal cell + 1
        # else it is the max of upper or lower cell

        dp = [[None for _ in range(n+1)] for _ in range(m+1)]
        
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            
            if text1[i] == text2[j]:
                if dp[i-1][j-1] == None:
                    dp[i-1][j-1] = helper(i-1, j-1)
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                if dp[i-1][j] == None:
                    dp[i-1][j] = helper(i-1, j)
                if dp[i][j-1] == None:
                    dp[i][j-1] = helper(i, j-1)
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            return dp[i][j]
        helper(m-1, n-1)
        return dp[m-1][n-1]