# -*- coding:utf-8 -*-


# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#  
# Example 1:
#
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # we can use dfs
        
        def dfs(i, j):
            if grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            if i + 1 < len(grid):
                dfs(i+1, j)
            
            if i - 1 >= 0:
                dfs(i-1, j)
            
            if j + 1 < len(grid[i]):
                dfs(i, j+1)
            
            if j-1 >= 0:
                dfs(i, j-1)
        count = 0       
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
                
                
                
            
        
