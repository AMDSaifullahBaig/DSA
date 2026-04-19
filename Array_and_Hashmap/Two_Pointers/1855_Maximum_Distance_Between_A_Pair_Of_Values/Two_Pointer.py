class Solution:
    def maxDistance(self, A: List[int], B: List[int]) -> int:
    	i=0
    	j=1
    	while i<len(A) and j<len(B):
    		if A[i]>B[j]:
    			i+=1
    		j+=1
    	return j-i-1