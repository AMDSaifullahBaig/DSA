from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
    	count=Counter(nums)
    	for i in count:
    		if count[i]==1:
    			return i