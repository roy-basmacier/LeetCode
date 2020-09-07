class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        edges = {} # x -> (y, weight)
        for x, y, w in flights:
            if x not in edges:
                edges[x] = []
                
            edges[x].append((y, w))
            
        
        heap = []
        heapq.heappush(heap, (0, src, K+1))
        # dijkstra
        while heap:
            price, current, stops = heapq.heappop(heap)
            
            if current is dst:
                return price
            if stops > 0:
                if current in edges:
                    for nextNode, nextPrice in edges[current]:
                        heapq.heappush(heap, (price + nextPrice, nextNode, stops-1))
                    
        return -1
        
        
        