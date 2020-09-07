class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i != 0 or j != 0:
                    grid[i][j] = min(grid[i - 1][j] if i - 1 >= 0 else float('inf'), grid[i][j - 1] if j - 1 >= 0 else float('inf')) + grid[i][j]
        return grid[len(grid)-1][len(grid[0])-1]
        # we can apply dijkstras algorithm     
#         # keeps track of the distance to get to that position (if not defined then it takes inf)
#         nodes = {(0,0):grid[0][0]}
#         i = 0 # y axis
#         j = 0 # x axis
#         unvisited = set()
#         unvisited.add((i,j))
#         while len(unvisited) > 0:
#             unvisited.remove((i, j))
#             if i + 1 < len(grid):
#                 if (i+1, j) not in nodes:
#                     unvisited.add((i+1, j))
#                     nodes[(i+1, j)] = nodes[(i,j)] + grid[i+1][j]
#                 else:
#                     nodes[(i+1,j)] = min(nodes[(i,j)] + grid[i+1][j], nodes[(i+1, j)])
            
#             if i - 1 >= 0:
#                 if (i-1, j) not in nodes:
#                     unvisited.add((i-1, j))
#                     nodes[(i-1, j)] = nodes[(i,j)] + grid[i-1][j]
#                 else:
#                     nodes[(i-1,j)] = min(nodes[(i,j)] + grid[i-1][j], nodes[(i-1, j)])
            
#             if j + 1 < len(grid[i]):
#                 if (i, j+1) not in nodes:
#                     unvisited.add((i, j+1))
#                     nodes[(i, j+1)] = nodes[(i,j)] + grid[i][j+1]
#                 else:
#                     nodes[(i,j+1)] = min(nodes[(i,j)] + grid[i][j+1], nodes[(i, j+1)])
            
#             if j-1 >= 0:
#                 if (i, j-1) not in nodes:
#                     unvisited.add((i, j-1))
#                     nodes[(i, j-1)] = nodes[(i,j)] + grid[i][j-1]
#                 else:
#                     nodes[(i,j-1)] = min(nodes[(i,j)] + grid[i][j-1], nodes[(i, j-1)])
#             currMin = None
#             for _i, _j in unvisited:
#                 if currMin == None or currMin > nodes[(_i, _j)]:
#                     currMin = nodes[(_i,_j)]
#                     i, j = _i, _j

#         return nodes[len(grid)-1, len(grid[0])-1]

            
        