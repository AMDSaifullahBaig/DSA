class Solution:
    def distance(self, nums: List[int]) -> List[int]:
    	hash=defaultdict(list)
    	for idx,val in enumerate(nums):
    		hash[val].append(idx)
    	result=[0]*len(nums)
    	for i in hash.values():
    		add=sum(i)
    		n=len(i)
    		prefix=0
    		for idx,val in enumerate(i):
    			result[val]=add-prefix*2+val*(2*idx-n)
    			prefix+=val
    	return result