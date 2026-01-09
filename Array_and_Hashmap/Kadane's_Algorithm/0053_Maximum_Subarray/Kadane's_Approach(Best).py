class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum=float('-inf')
        current=0
        for i in nums:
            current=i+current
            if current>maximum:
                maximum=current
            if current<0:
                current=0
        return maximum