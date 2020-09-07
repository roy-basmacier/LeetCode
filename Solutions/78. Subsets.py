class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            n = len(res)
            for i in range(n):
                res.append(res[i] + [num])
        return res