class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0
        count = 0
        product = 1
        
        j = 0
        for i in range(len(nums)):
            product *= nums[i]
            
            #if the product is too big adjust the window 
            while product >= k:
                product /= nums[j]
                j += 1
            count += i - j + 1  
        return count