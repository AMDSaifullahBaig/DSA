class Solution:
    def concatenatedBinary(self, n: int) -> int:
    	result=0
    	mod=10**9+7
    	for i in range(1,n+1):
    		length=bit_length(i)
    		result=(result<<length)+i
    	return result%mod