class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        minimum=float("inf")
        hash={}
        for i in range(len(nums)):
        	e=nums[i]
        	if e not in hash:
        		hash[e]=[i]
        	else:
        		hash[e]. append(i)
        for e in hash.values():
        	if len(e)<3:
        		continue
        	for i in range(len(e)-2):
        		curr=(e[i+2]-e[i])*2
        		minimum=min(minimum,curr)
        return -1 if minimum==float("inf") else minimum