class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # traverse the array
        # keep track of the previous numbers
        # if the previous number is greater than the current number
        # delete the previous number
        if len(num) <= k:
            return '0'
        
        prvNums = [] # Stack
        for ch in num:
            while prvNums != [] and k > 0 and prvNums[-1] > ch:
                prvNums.pop()
                k -= 1
            prvNums.append(ch)
            
        if k > 0:
            prvNums = prvNums[:-k]
        
        # get rid of leading zeros
        res = ''
        i = 0
        while i < len(prvNums) and prvNums[i] == '0':
            i += 1
        
        while i < len(prvNums):
            res += prvNums[i]
            i += 1
            
        if len(res) == 0:
            res = '0'
        return res
        
        