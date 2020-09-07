class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0 for _ in range(rowIndex+1)]
        res[0] = 1
        for i in range(rowIndex):
            for j in range(i+1, -1, -1):
                res[j] += res[j-1]
        res[0] = 1
        return res
        