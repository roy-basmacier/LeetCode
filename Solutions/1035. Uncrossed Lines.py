class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # Time  Complexity -> O(nm)
        # Space Complexity -> O(nm)

        # dynamic programming
        #Input: A = [1,4,2], B = [1,2,4]
        #   1 4 2
        # 1 1 1 1
        # 2 1 0 2  
        # 4 1 2 0
        
        #   1 4 1
        # 1 1 1 1
        # 2 1 1 1
        # 4 1 2 2
        
        # Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
        #   10 5 2 1 5 2
        # 2  0 0 1 1 1 1
        # 5  0 1 1 1 1 1
        # 1  0 1 1 2 2 2
        # 2  0 1 1 2 2 3  
        # 5  0 1 1 2 3 3
        
        
        dp = [0] * (len(B)+1)
        for i in range(len(A)):  
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[j+1] = dp[j] + 1
            for j in range(len(B)):
                dp[j+1] = max(dp[j+1], dp[j])
                
        
        return dp[len(B)]