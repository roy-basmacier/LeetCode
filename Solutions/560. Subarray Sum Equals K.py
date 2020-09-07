class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        Sum = 0
        sumMap = {Sum:1}
        for num in nums:
            Sum += num
            if Sum - k in sumMap:
                count += sumMap[Sum -k]
            if Sum not in sumMap:
                sumMap[Sum] = 0
            sumMap[Sum] += 1
        return count