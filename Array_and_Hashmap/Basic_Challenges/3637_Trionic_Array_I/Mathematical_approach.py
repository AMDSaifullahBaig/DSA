class Solution(object):
    def isTrionic(self, nums):
    	if nums[0]>nums[1]:
    		return False
    	c=0
    	n=len(nums)
    	for i in range(2,n):
    		if nums[i-1]==nums[i]:
    			return False
    		if ((nums[i-2]-nums[i-1])*(nums[i-1]-nums[i]))<0:
    			c+=1
    	return c==3