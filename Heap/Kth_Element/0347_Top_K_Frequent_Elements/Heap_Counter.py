class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    	l=[]
    	counts=Counter(nums)
    	counts=[(-freq,num) for num,freq in counts.items()]
    	heapify(counts)
    	for i in range(k):
    		e=heappop(counts)
    		l.append(e[1])
    	return l