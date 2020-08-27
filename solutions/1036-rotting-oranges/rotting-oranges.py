# -*- coding:utf-8 -*-


# In a given grid, each cell can have one of three values:
#
#
# 	the value 0 representing an empty cell;
# 	the value 1 representing a fresh orange;
# 	the value 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
#
#  
#
#
# Example 1:
#
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
#
# Example 2:
#
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
#
#
# Example 3:
#
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
#  
#
# Note:
#
#
# 	1 <= grid.length <= 10
# 	1 <= grid[0].length <= 10
# 	grid[i][j] is only 0, 1, or 2.
#
#
#
#
#


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def allRotten():
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        return False
            return True
        
        
        def updateOranges(r, c):
            canRot = False
            for row, col in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                    grid[row][col] = 3
                    canRot = True
            return canRot
            
            
        def finishRotting():
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
                        
                        
                        
        time = 0
        
        rotting = True
        while rotting:
            continueRot = False
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 2:
                        continueRot |= updateOranges(r, c)
                        
            time += 1
            finishRotting()
            rotting = continueRot
        if allRotten():
            return time-1
        return -1
            
            
                        
            
            
        
