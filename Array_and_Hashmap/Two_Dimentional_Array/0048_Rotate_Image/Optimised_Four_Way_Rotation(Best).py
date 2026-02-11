class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for row in range((n+1)//2):
            for column in range(n//2):
                temp=matrix[row][column]
                matrix[row][column]=matrix[n-1-column][row]
                matrix[n-1-column][row]=matrix[n-1-row][n-1-column]
                matrix[n-1-row][n-1-column]=matrix[column][n-1-row]
                matrix[column][n-1-row]=temp