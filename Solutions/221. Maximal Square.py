class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        dp = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        for i in range(1, len(matrix)):
            for  j in range(1, len(matrix[0])):
                if dp[i][j] != 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        maxArea = max(max(row) for row in dp)
        return maxArea ** 2
                    