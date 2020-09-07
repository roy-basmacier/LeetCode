class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        costs = sorted(costs, key= lambda x: x[0] - x[1])
        res = 0
        for a, b in costs[:n/2]:
            res += a
        for a, b in costs[n/2:]:
            res += b
        return res
            
        