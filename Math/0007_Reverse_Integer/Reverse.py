class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
        	sign=-1
        	x*=-1
        else:
        	sign=1
        result=0
        while x:
        	result=result*10+x%10
        	x//=10
        if sign==-1:
        	result*=-1
        if result>2**31-1 or result<-2**31-1:
        	return 0
        return result