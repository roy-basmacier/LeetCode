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
                    
                
            