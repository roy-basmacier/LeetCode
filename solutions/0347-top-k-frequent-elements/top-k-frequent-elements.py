# -*- coding:utf-8 -*-


# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Note: 
#
#
# 	You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# 	Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# 	It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# 	You can return the answer in any order.
#
#


import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # create a count dictionary -> O(n)
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        # heapify the values of out dictionary -> O(q) = O(n), q-> unique elements in nums
        heap = [(-cnt, num) for num, cnt in count.items()]
        heapq.heapify(heap)
        res = []
        
        # pop from heap to get k frequent number -> O(k * log(n))
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
