class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        # copying the list to use it after modifying it
        orj = nums.copy()
        even = 0
        odd = 0
        # checking the min moves for even indexes
        for i in range(0,len(nums),2):
            if i-1 >= 0 and  nums[i] <= nums[i-1]:
                even += nums[i-1] - nums[i] + 1
                nums[i-1] = nums[i]-1
                
            if i+1 < len(nums) and  nums[i] <= nums[i+1]:
                even += nums[i+1] - nums[i] + 1
                nums[i+1] = nums[i]-1
            
        # nums was modified so we reset it to it's original form
        nums = orj 
        # checking the min moves for odd indexes
        for i in range(1,len(nums), 2):
            # checking if the previous number is greater then the current number
            if i-1 >= 0 and  nums[i] <= nums[i-1]:
                odd += nums[i-1] - nums[i] + 1
                nums[i-1] = nums[i]-1
                
            # checking if the next number is greater than the current number
            if i+1 < len(nums) and  nums[i] <= nums[i+1]:
                odd += nums[i+1] - nums[i] + 1
                nums[i+1] = nums[i]-1
        return min(odd, even)
            
        