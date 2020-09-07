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
            
            
                        
            
            
        