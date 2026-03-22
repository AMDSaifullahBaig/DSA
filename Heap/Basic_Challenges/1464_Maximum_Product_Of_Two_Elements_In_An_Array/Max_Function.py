class Solution:
    def maxProduct(self, nums: List[int]) -> int: 
        max1=max(nums)
        nums.remove(max1)
        return (max1-1)*(max(nums)-1)