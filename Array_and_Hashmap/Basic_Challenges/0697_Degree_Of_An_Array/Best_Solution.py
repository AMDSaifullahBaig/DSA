from collections import Counter
class Solution(object):
    def findShortestSubArray(self, nums):
    	start={}
    	stop={}
    	count={}
    	for idx,val in enumerate(nums):
    		if val not in start:
    			start[val]=idx
    		count=count.get(val,0)+1
    		stop[val]=idx
    	maximum=max(count.values())
    	answer=len(nums)
    	for val in count:
    		if val==maximum:
    			answer=min( answer,stop[val]-start[val]+1)
    	return answer