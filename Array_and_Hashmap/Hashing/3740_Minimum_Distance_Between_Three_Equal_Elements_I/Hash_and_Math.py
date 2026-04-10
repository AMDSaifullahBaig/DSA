class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
    	minimum=float("inf")
    	hash={}
    	for i in range(len(nums)):
    		if nums[i] in hash:
    			hash[nums[i]].append(i)
    		else:
    			hash[nums[i]]=[i]
    	for i in hash.values():
    		if len(i)<3:
    			continue 
    		else:
    			for j in range(len(i)-2):
    				minimum=min(minimum,2*(i[j+2]-i[j]))
    	return -1 if minimum==float("inf") else minimum