class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
    	robot.sort()
    	factory.sort()
    	inf=float("inf")
    	m=len(robot)
    	n=len(factory)
    	dp=[[inf]*(n+1) for i in range(m+1)]
    	for j in range(n+1):
    		dp[0][j]=0
    	for j in range(1,n+1):
    		position,capacity=factory[j-1]
    		for i in range(m+1):
    			distance=0
    			dp[i][j]=dp[i][j-1]
    			for k in range(1,min(i,capacity)+1):
    				distance+=abs(robot[i-k]-position)
    				dp[i][j]=min(dp[i][j],dp[i-k][j-1]+distance)
    	return dp[m][n]