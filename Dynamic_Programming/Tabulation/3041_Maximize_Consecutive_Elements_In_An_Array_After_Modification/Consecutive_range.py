class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        dp=[0]*(nums[-1]+2)
        for i in nums:
            dp[i+1]=dp[i]+1
            dp[i]=dp[i-1]+1
        return max(dp)