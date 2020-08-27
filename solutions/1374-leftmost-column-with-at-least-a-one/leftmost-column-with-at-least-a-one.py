# -*- coding:utf-8 -*-


# (This problem is an interactive problem.)
#
# A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.
#
# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
#
# You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
#
#
# 	BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
# 	BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
#
#
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.
#
# For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.
#
#  
#
#  
#
#  
# Example 1:
#
#
#
#
# Input: mat = [[0,0],[1,1]]
# Output: 0
#
#
# Example 2:
#
#
#
#
# Input: mat = [[0,0],[0,1]]
# Output: 1
#
#
# Example 3:
#
#
#
#
# Input: mat = [[0,0],[0,0]]
# Output: -1
#
# Example 4:
#
#
#
#
# Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	rows == mat.length
# 	cols == mat[i].length
# 	1 <= rows, cols <= 100
# 	mat[i][j] is either 0 or 1.
# 	mat[i] is sorted in a non-decreasing way.
#


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        # search from top right to bottom left
        n, m = binaryMatrix.dimensions()
        row = 0
        col = n-1
        answer = -1
        while row < n and col >= 0:
            cell = binaryMatrix.get(row, col)
            if cell == 1:
                answer = col
                col -= 1
            else:
                row += 1
        return answer
            
        
