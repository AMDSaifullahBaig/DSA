class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        n=max(nums)
        point=[0]*(n+1)
        for i in nums:
            point[i]+=i
        dp=[0]*(n+1)
        dp[1]=point[1]
        for i in range(2,n+1):
            skip=dp[i-1]
            dp[i]=max(skip,dp[i-2]+point[i])
        return dp[n]