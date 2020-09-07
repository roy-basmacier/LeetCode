class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        i = 0
        while i < len(nums)-2:
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                pass
            else:
                l, r = i+1, len(nums)-1

                while l < r:
                    totalSum = nums[i] + nums[l] + nums[r]
                    if totalSum < 0:
                        l += 1
                    elif totalSum > 0:
                        r -= 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
            i += 1
        return res
            
            
            
                
        
        