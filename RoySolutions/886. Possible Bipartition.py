class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        
        # creating the graph
        graph = {} # node -> vertices (list)
        
        for a, b in dislikes:
            if a not in graph:
                graph[a] = [b]
            else:
                graph[a].append(b)
            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)
        
        label = {}
        def dfs(node, expected_label=0):
            if node in label:
                return label[node] == expected_label
            
            label[node] = expected_label
            res = True
            for v in graph[node]:
                res &= dfs(v, (expected_label + 1)%2)
            return res
        res = True
        for v in range(1, N+1):
            if v not in label and v in graph:
                res &=dfs(v)
        return res
        
        
        