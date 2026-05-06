class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m=len(boxGrid)
        n=len(boxGrid[0])
        result=[["." for i in range(m)] for j in range(n)]
        for i in range(m):
        	last=n-1
        	for j in range(n-1,-1,-1):
        		if boxGrid[i][j]=="#":
        			result[last][m-1-i]="#"
        			last-=1
        		if boxGrid[i][j]=="*":
        			boxGrid[j][m-i-1]="*"
        			last=j-1
        return result