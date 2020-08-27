# -*- coding:utf-8 -*-


# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
#  
# Constraints:
#
#
# 	board and word consists only of lowercase and uppercase English letters.
# 	1 <= board.length <= 200
# 	1 <= board[i].length <= 200
# 	1 <= word.length <= 10^3
#
#


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
                
    
    
    
        
