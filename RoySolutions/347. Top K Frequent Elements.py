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
        