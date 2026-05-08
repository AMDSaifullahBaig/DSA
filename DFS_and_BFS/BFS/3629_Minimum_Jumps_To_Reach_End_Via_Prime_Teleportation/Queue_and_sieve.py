limit=1000001
factor=[[] for i in range(limit)]
for i in range(2,limit):
	for j in range(i,limit,i):
		factor[j].append(i)
class Solution:
    def minJumps(self, nums: List[int]) -> int:
    	edge=defaultdict(list)
    	n=len(nums)
    	for idx,val in enumerate(nums):
    		for fac in factor[val]:
    			edge[fac].append(idx)
    	result=0
    	queue=[0]
    	seen=[False]*n
    	seen[0]=True
    	while True:
    		temp_queue=[]
    		for i in queue:
    			if i==n-1:return result
    			if i>0 and not seen[i-1]:
    				seen[i-1]=True
    				temp_queue.append(i-1)
    			if i<n-1 and not seen[i+1]:
    				seen[i+1]=True
    				temp_queue. append(i+1)
    			if len(factor[nums[i]])==1 and factor[nums[i]][0]==nums[i]:
    				for j in edge[nums[i]]:
    				            if not seen[j]:
    				            	seen[j]=True
    				            	temp_queue.append(j)
    				edge[nums[i]]=[]
    		queue=temp_queue
    		result+= 1