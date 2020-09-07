class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time  Complexity -> O(n)
        # Space Complexity -> O(n)
        difference = {}
        for i, num in enumerate(nums):
            difference[target-num] = i
            
        for i, num in enumerate(nums):
            if num in difference and i != difference[num]:
                return [i, difference[num]]
