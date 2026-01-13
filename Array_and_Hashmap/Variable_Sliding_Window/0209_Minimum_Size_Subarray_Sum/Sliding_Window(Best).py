class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        length=len(nums)
        l=0
        minimum=float('inf')
        summation=0
        for r in range(length):
            summation+=nums[r]
            while summation>=target:
                minimum=min(minimum,r-l+1)
                summation-=nums[l]
                l+=1
        return 0 if minimum==float('inf') else minimum