class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        res = ''
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                for k, z in enumerate(A):
                    if i != j and i != k and j != k:
                        hour = str(x) + str(y)
                        minute = str(z) + str(A[6-i-j-k])
                        if hour < '24' and minute < '60':
                            res = max(res,hour + ':' + minute)
        return res
        
        
        
        
        
                
        
            
                
            