class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr=[]
        count=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
        	for j in range(n):
        		arr.append(grid[i][j])
        arr.sort()
        median=arr[len(arr)//2]
        for i in arr:
        	if i%x!=median%x:return -1
        	count+=abs(median-i)//x
        return count