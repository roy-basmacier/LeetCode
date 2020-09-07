class Solution(object):
   
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(row, col, wordIndex):
            if wordIndex == len(word):
                return True
            visited[row][col] = 1
            res = False
            for nextRow, nextCol in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                if 0 <= nextRow < len(board) and 0 <= nextCol < len(board[0])\
                and visited[nextRow][nextCol] == 0 and board[nextRow][nextCol] == word[wordIndex]:
                    res = res or dfs(nextRow, nextCol, wordIndex + 1)
            visited[row][col] = 0
            return res
        
        if not word:
            return True
        
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 1):
                        return True
            
        return False
                
    
    
    
        