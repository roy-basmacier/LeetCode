class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # Time Complexity -> O(n)
        # Spce Complexity -> O(1)
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
        
        