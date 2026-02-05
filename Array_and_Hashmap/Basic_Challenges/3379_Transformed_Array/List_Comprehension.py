class Solution(object):
    def constructTransformedArray(self, nums):
        n=len(nums)
        return [nums[((nums[i]+i)%n+n)%n] for i in range(n)]