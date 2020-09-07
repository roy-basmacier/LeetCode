class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        queue = [[0]]
        while queue:
            path = queue.pop()
            num = path[-1]
            for nextNode in graph[num]:
                temp = path + [nextNode]
                queue.append(temp)
                if nextNode == len(graph)-1:
                    res.append(temp)
        return res
            