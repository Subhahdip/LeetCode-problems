class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #transpose of the matrix
        for i in range(len(matrix)):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        #reverse the rows        
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        
