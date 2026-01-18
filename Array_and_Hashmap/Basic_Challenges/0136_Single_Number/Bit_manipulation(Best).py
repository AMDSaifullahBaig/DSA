class Solution(object):
    def singleNumber(self, nums):
    	c=0
    	for i in nums:
    		c^=i
    	return c