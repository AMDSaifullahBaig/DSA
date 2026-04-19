class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        for i in range(n-1,0,-1):
        	if colors[0]!=colors[i]:
        		maximum=i
        		break
        for i in range(n):
        	if colors[n-1]!=colors[i]:
        		return max(maximum,n-1-i)