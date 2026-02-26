class Solution:
    def numSteps(self, s: str) -> int:
        c=0
        s=int(s,2)
        while s!=1:
        	if s&1:
        		s+=1
        	else:
        		s//=2
        	c+=1
        return c