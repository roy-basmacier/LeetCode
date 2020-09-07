class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        citizens = [0] * (N+1)
        for a, b in trust:
            citizens[a] -= 1
            citizens[b] += 1
        
        for i in range(1, N+1):
            if citizens[i] == N-1:
                return i
        return -1
                
            
        