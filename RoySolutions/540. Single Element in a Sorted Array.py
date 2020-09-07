class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Modify Binary Search
        # modifications:
        # Let the size of the window/array = N
        # if N % 4 == 1:
        #   look at the middle number
        #   if the number to the left of middle is the same then the unique is on the left hand side
        #   1 1 2 3 (3) 4 4 8 8 -> unique is 2 and middle is (3) left of it is also 3 so check leftside
        #   vise versa for right hand side
        #   1 1 3 3 (4) 4 6 8 8 -> unique is 6 and middle is (4) right of it is 4 so unique is on left side
        #   if the left and the right of middle is different then thats our unique
        #   1 1 (2) 3 3 -> return middle since left and right side is not equal to middle
        # when N % 4 == 3:
        # then the above thing is reversed

        left = 0
        right = len(nums)-1
        while left < right:
            N = right-left + 1
            middle = (left+right)//2
            if N == 3:
                if nums[middle] == nums[middle-1]:
                    return nums[middle+1]
                elif nums[middle] == nums[middle+1]:
                    return nums[middle-1]
                else:
                    return nums[middle] 
            if N % 4 == 1:
                if nums[middle] == nums[middle-1]:
                    right = middle-2
                elif nums[middle] == nums[middle+1]:
                    left = middle+2
                else:
                    return nums[middle]
            else: # N % 4 == 3
                if nums[middle] == nums[middle+1]:
                    right = middle-1
                elif nums[middle] == nums[middle-1]:
                    left = middle+1
                else:
                    return nums[middle]
                
        return nums[left]
        