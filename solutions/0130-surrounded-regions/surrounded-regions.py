# -*- coding:utf-8 -*-


# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
#


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Call a dps on each O thats on the edge
        # convert those in the dfs from Os to Xs
        
        # Time complexity -> O(n*m)
        # Space complexity -> O(n*m)  = O(h) where h is the height of the dfs tree
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        def dfs(row, col):
            visited[row][col] = 1
            for nextRow, nextCol in [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]:
                if  0 <= nextRow < len(board) \
                and 0 <= nextCol < len(board[row])\
                and board[nextRow][nextCol] == 'O'\
                and visited[nextRow][nextCol] == 0:
                    dfs(nextRow, nextCol)
            
        
        # border 
        # -> row is first or last
        # -> col is first or last
        for row in range(len(board)):
            for col in range(len(board[row])):
                #if border
                if (row == 0 or row == len(board)-1 \
                or col == 0 or col == len(board[row])-1)\
                and board[row][col] == 'O':
                    dfs(row, col)
                    
       
        for row in range(len(board)):
            for col in range(len(board[row])):
                if visited[row][col] == 0:
                    board[row][col] = 'X'
                
        
