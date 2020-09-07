class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        res = 0
        for i, j in enumerate(sorted(citations, reverse=True)):
            if i < j:
                res += 1
                
        return res