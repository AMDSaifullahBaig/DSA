class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        hash=DefaultDict(list)
        result=[]
        n=len(nums)
        for idx,val in enumerate(nums):
        	hash[val].append(idx)
        for q in queries:
        	val=hash[nums[q]]
        	if len(val)<=1:
        		result.append(-1)
        		continue 
        	position=bisect_left(val,q)
        	curr=float("inf")
        	
        	left=val[(position-1)%len(val)]
        	d1=abs(q-left)
        	curr=min(curr,min(d1,n-d1))
        	
        	right=val[(position+1)%len(val)]
        	d2=abs(q-right)
        	curr=min(curr,min(d2,n-d2))
        	
        	result.append(curr)
        return result