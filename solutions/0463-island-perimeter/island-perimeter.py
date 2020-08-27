# -*- coding:utf-8 -*-


# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
#  
#
# Example:
#
#
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Output: 16
#
# Explanation: The perimeter is the 16 yellow stripes in the image below:
#
#
#
#


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def dfs(i, j):
            visited[i][j] = 1
            cnt = 0
            for next_i, next_j in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                if len(grid) > next_i >= 0 and len(grid[0]) > next_j >= 0:
                    if grid[next_i][next_j] == 1:
                        if visited[next_i][next_j] == 0:
                            cnt += dfs(next_i, next_j)
                    else:
                        cnt += 1
                else:
                    cnt += 1
            return cnt
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    res = dfs(i,j)
        return res
                    
                
            
