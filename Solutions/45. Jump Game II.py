class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # greedy approach 
        # choose the best jump by evaluating:
        # next Jump value + next jump index
        # we will pick the max one and go from there
        jumpCount = 0
        i = 0
        while i < len(nums)-1:
            bestJump = 0
            nextI = i+1
            currentJump = nums[i]
            for nextJump in range(1, currentJump + 1):
                jumpIndex = i + nextJump
                if jumpIndex >= len(nums) -1:
                    return jumpCount + 1
                if bestJump < nextJump + nums[jumpIndex]:
                    bestJump = nextJump + nums[jumpIndex]
                    nextI = jumpIndex
            i = nextI
            jumpCount += 1
            
            
        return jumpCount