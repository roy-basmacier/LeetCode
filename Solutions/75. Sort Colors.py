class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0] # Red, White, Blue
        for color in nums:
            count[color] += 1
            
        i = 0
        for color, freq in enumerate(count):
            for _ in range(freq):
                nums[i] = color
                i += 1
                
            
            