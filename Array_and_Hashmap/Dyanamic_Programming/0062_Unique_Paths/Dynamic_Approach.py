class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(x,y,cache):
        	if x==0 and y==0:
        		return 1
        	if x<0 or y<0:
        		return 0
        	if cache[x][y]!=-1:
        		return cache[x][y]
        	up=dp(x,y-1,cache)
        	left=dp(x-1,y,cache)
        	cache[x][y]=up+left
        	return cache[x][y]
        cache=[[-1 for i in range(n)]for j in range(m)]
        return dp(m-1,n-1,cache)