class Solution(object):
    def majorityElement(self, nums):
        result=0
        sum=0
        for i in nums:
        	if sum==0:
        		result=i
        	if result==i:
        		sum+=1
        	else:
        		sum-=1
        return result 