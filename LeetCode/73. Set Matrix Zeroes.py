"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
"""
# Solution 1: Brute: Time: 2* O(m * n) + O(m + n) Space: O(1)
class Solution:
    def markRow(self,matrix, cols, r):
        for c in range(cols):
            if matrix[r][c] != 0:
                matrix[r][c] = None
    def markCol(self,matrix, rows, c):
        for r in range(rows):
            if matrix[r][c] != 0:
                matrix[r][c] = None
                
    def setZeroes(self, matrix: List[List[int]]) -> None:
     
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    self.markRow(matrix, cols, r)
                    self.markCol(matrix, rows, c)
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == None:
                    matrix[r][c] =0

# Solution 2: Better: Time: 2* O(m * n) Space: O(m + n) 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        total_rows = len(matrix)
        total_cols = len(matrix[0])

        aux_rows = [0] * total_rows
        aux_cols = [0] * total_cols

        for row in range(total_rows):
            for cols in range(total_cols):
                if matrix[row][cols] == 0:
                    aux_rows[row] = 1
                    aux_cols[cols] = 1

        for row in range(total_rows):
            for cols in range(total_cols):
                if aux_rows[row] == 1 or aux_cols[cols] == 1:
                    matrix[row][cols] = 0
        return matrix

# Solution 2: Optimal: Time: 2* O(m * n) Space: O(1) 
class Solution:

                
    def setZeroes(self, matrix: List[List[int]]) -> None:
     
        rows = len(matrix)
        cols = len(matrix[0])
        col0 = 1
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0

                    if c == 0:
                        col0 = 0
                    else:
                        matrix[0][c] = 0

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for c in range(cols): 
                matrix[0][c] = 0
        if col0 == 0:
            for r in range(rows):
                matrix[r][0] = 0

        
