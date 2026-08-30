class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        minimum=nums.index(min(nums))
        maximum=nums.index(max(nums))
        if maximum<minimum:
            first=maximum
            second=minimum
        else:
            first=minimum
            second=maximum
        return min(second+1,n-first,first+1+n-second)