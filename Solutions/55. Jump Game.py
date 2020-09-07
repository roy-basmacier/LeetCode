class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxJump = 1 # number of hops remaining
        
        # iterate over array and decrease maxJump by one after each iteration
        # compare the maxJump  and the ith value at array and choose which ones higher
        for i in range(len(nums)):
            maxJump -= 1
            if maxJump < 0:
                return False
            maxJump = max(maxJump, nums[i])
            
        return True
        