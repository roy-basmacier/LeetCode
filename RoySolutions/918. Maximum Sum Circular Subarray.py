class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res1 = curr = None
        for num in A:
            curr = max(curr, 0) + num
            res1 = max(res1, curr)
        
        res2 = curr = float('inf')
        for i in range(1, len(A)):
            curr = A[i] + min(curr, 0)
            res2 = min(res2, curr)
        res2 = sum(A) - res2
        
        res3 = curr = float('inf')
        for i in range(len(A)-1):
            curr = A[i] + min(curr, 0)
            res3 = min(res3, curr)
        res3 = sum(A) - res3
        
        return max(res1, res2, res3)
        