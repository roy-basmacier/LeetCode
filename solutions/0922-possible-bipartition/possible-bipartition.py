# -*- coding:utf-8 -*-


# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the same group. 
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this way.
#
#  
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
#
#
#
# Example 2:
#
#
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
#
#
#
# Example 3:
#
#
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
#
#
#
#
#  
# Constraints:
#
#
# 	1 <= N <= 2000
# 	0 <= dislikes.length <= 10000
# 	dislikes[i].length == 2
# 	1 <= dislikes[i][j] <= N
# 	dislikes[i][0] < dislikes[i][1]
# 	There does not exist i != j for which dislikes[i] == dislikes[j].
#


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
        
        
        
