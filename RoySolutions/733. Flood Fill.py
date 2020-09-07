class Solution(object):
            
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(i, j, prvColor):
            image[i][j] = newColor
            for x, y in ((0,1), (0,-1), (1,0), (-1,0)):
                if  0 <= i + x < len(image) and 0 <= j + y < len(image[0]) and image[i+x][j+y] == prvColor and prvColor != newColor:
                    dfs(i+x, j+y, prvColor)
                
        dfs(sr, sc, image[sr][sc])
        
        return image
        
        