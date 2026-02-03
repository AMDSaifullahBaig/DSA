class Solution(object):
    def isTrionic(self, nums):
    	n=len(nums)
    	i=1
    	while (i<n and nums[i-1]<nums[i]):
    		c+=1
    	f=i-1
    	while (i<n and nums[i-1]>nums[i]):
    		c+=1
    	s=i-1
    	while (i<n and nums[i-1]<nums[i]):
    		c+=1
    	t=i-1
    	return (f!=0 and f!=s and (t==n-1 and t!=s))