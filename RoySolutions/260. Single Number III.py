class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Set = set()
        for num in nums:
            if num not in Set:
                Set.add(num)
            else:
                Set.remove(num)
        return list(Set)
        