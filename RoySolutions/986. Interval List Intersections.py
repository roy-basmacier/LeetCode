class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        a = 0
        b = 0
        output = []
        while a < len(A) and  b < len(B):
            aStart = A[a][0]
            aEnd = A[a][1]
            bStart = B[b][0]
            bEnd = B[b][1]
            
            outStart = max(aStart, bStart)
            outEnd = min(aEnd, bEnd)
            if outStart <= outEnd:
                output.append((outStart, outEnd))
                
            if aEnd > bEnd:
                b += 1
            else:
                a += 1
        return output