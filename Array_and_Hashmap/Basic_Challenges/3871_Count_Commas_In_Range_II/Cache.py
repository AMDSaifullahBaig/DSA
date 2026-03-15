class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        cache=[]
        for i in range(1,len(nums)):
            num=nums[i]-nums[i-1]
            if nums not in hash:
            	hash[(i-1,i)]=num
            else:
            	for i in cache:
            		if cache[i]!=num:
            			return cache[i]