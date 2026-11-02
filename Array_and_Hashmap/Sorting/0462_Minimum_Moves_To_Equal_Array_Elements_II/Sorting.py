class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        m=len(nums)//2
        median=nums[m]
        l=sum(nums[:m+1])
        r=sum(nums[m+1:])
        return ((m+1)*median-l)+(r-(len(nums)-m-1)*median)