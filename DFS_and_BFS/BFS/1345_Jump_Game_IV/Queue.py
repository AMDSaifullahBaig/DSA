class Solution:
    def minJumps(self, arr: List[int]) -> int:
        hash={}
        step=0
        for i in range(len(arr)):
        	if arr[i] not in hash:
        		hash[arr[i]]=[i]
        	else:
        		hash[arr[i]].append(i)
        queue=[0]
        while queue:
        	next=[]
        	for i in queue:
        		if i==len(arr)-1:return step
        		if arr[i]=="#":continue
        		if arr[i] in hash:
        			val=arr[i]
	        		for j in hash[val]:
	        			if arr[j]!="#":
	        				next.append(j)
	        		hash[val].clear()
        		for j in [i+1,i-1]:
        			if 0<=j<len(arr) and arr[j]!="#":
        				next.append(j)
        		arr[i]="#"
        	queue=next
        	step+=1
        return step