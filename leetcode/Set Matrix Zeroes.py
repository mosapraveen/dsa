class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        zero=[]
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    zero.append((i,j))
        for i,j in zero:
            for col in range(n):
                matrix[i][col]=0
            for row in range(m):
                matrix[row][j]=0
