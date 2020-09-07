import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = {}
        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1
        
        longest = max(freq.values())
        res = (longest - 1) * (n+1)
        for count in freq.values():
            if count == longest:
                res += 1
        return max(res, len(tasks))