class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        maximum=-1
        minimum=nums[0]
        for i in range(1,n):
        	if nums[i]>minimum:
        		maximum=max(maximum,nums[i]-minimum)
        	else:
        		minimum=nums[i]
        return maximum