class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        
        memo = {}
        # populate memo
        for i in range(0, 10):
            # check i + k and i - k
            key = str(i)
            memo[key] = []
            
            if i + K < 10:
                # find number
                memo[key].append(str(i+K))
                
            if abs(i - K) < 10 and  abs(i-K) == i - K:
                # find number
                memo[key].append(str(abs(i-K)))
            
                
        res = set()
        stack = [str(i) for i in range(1,10)]
        if N == 1:
            stack.append("0")
        while stack:
            s = stack.pop()
            if len(s) == N:
                res.add(s)
            else:
                
                for nextCh in memo[s[-1]]:
                    stack.append(s+nextCh)
        return res
            
            
            
            
        
        