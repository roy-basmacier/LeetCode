class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxLength = 0
        d = {0: 0}
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
                
            if count not in d:
                d[count] = i + 1
            else:
                maxLength = max(maxLength, i+1-d[count])
        return maxLength
        