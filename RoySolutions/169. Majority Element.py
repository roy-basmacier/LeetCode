class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
            
        result = None
        cnt = 0
        for num, count in freq.items():
            if count > cnt:
                cnt = count
                result = num
        return result
        