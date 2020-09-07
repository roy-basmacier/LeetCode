class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            #index where nums[i] i suppose to be
            j = nums[i] - 1
            
            #swapping
            nums[i], nums[j] = nums[j], nums[i]
            
            #checking if nums[i] needs to swapped or not
            if nums[i]-1 == i or nums[i] == nums[nums[i]-1]:
                i += 1
        result = []
        for i in range(len(nums)):
            if i+1 != nums[i]:
                result.append(i+1)
        return result