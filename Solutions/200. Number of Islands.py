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
                
                
                
            
        