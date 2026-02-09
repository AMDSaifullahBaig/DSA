class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(start,stop,target):
            middle=(start+stop)//2
            if start>stop:
                return False
            row=middle//n
            column=middle%n
            print(row,column)
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]<target:
                return binary(middle+1,stop,target)
            else:
                return binary(start,middle-1,target)
        m=len(matrix)
        n=len(matrix[0])
        return binary(0,(m*n)-1,target)