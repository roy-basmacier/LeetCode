# -*- coding:utf-8 -*-


# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
#  
#
#
# Example 1:
#
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 5000
# 	0 <= A[i] <= 5000
#
#
#


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(A)-1
        while left < right:
            while left < len(A) and A[left] % 2 == 0:
                left += 1
            while right >= 0 and  A[right] % 2 == 1:
                right -= 1
                
            if left < right:
                A[left], A[right] = A[right], A[left]
        return A
        
        '''
        # Time complexity -> O(n)
        # Space complexty -> O(n)
        evenList = []
        oddList = []
        
        for num in A:
            if num % 2 == 0:
                evenList.append(num)
            else:
                oddList.append(num)
        return evenList + oddList
        '''
        
        
