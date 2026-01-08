class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix=0
        minimum=0
        maximum=float('-inf')
        for i in range(len(nums)):
            prefix+=nums[i]
            maximum=max(maximum,prefix-minimum)
            minimum=min(minimum,prefix)
        return maximum