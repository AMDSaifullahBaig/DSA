class Solution:
    def minimumDistance(self, word: str) -> int:
    	n=len(word)
    	inf=float("inf")
    	dp=[[[inf]*26 for i in range(26)] for j in range(n)]
    	for i in range(26):
    		dp[0][i][ord(word[0])-65]=0
    		dp[0][ord(word[0])-65][i]=0
    	for i in range(1,n):
    		curr=ord(word[i])-65
    		prev=ord(word[i-1])-65
    		d=self.distance(curr,prev)
    		for j in range(26):
    			dp[i][curr][j]=min(dp[i][curr][j],dp[i-1][prev][j]+d)
    			dp[i][j][curr]=min(dp[i][j][curr],dp[i-1][j][prev]+d)
    			if prev==j:
    				for k in range(26):
    					d0=self.distance(k,curr)
    					dp[i][curr][j]=min(dp[i-1][k][j]+d0  ,dp[i][curr][j])
    					dp[i][j][curr]=min(dp[i-1][j][k]+d0  ,dp[i][j][curr])
    	return min(min(dp[n-1][x]) for x in range(26))
    def distance(self,a,b):
    	r1,c1=a//6,a%6
    	r2,c2=b//6,b%6
    	return abs(r1-r2)+abs(c1-c2)