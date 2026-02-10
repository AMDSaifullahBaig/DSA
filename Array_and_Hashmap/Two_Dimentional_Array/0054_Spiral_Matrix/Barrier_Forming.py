class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        up=0
        down=m-1
        right=n-1
        left=0
        result=[]
        while up<=down and right>=left:
            for i in range(left,right+1):
                result.append(matrix[up][i])
            up+=1
            for i in range(up,down+1):
                result.append(matrix[i][right])
            right-=1
            if not(up<=down and left<=right):
                break
            for i in range(right+1,left,-1):
                result.append(matrix[down][i-1])
            down-=1
            for i in range(down+1,up,-1):
                result.append(matrix[i-1][left])
            left+=1
        return result