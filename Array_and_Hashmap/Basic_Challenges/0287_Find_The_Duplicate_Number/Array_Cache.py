class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cache=[0]*len(nums)
        for i in nums:
            if cache[i]==1:return i
            cache[i]=1