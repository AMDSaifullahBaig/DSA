class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        i=0
        n=len(s)
        while i<n:
        	l=i
        	r=min(i+k-1,n-1)
        	while l<r:
        		temp=s[l]
        		s[l]=s[r]
        		s[r]=temp
        		l+=1
        		r-=1
        	i+=2*k
        return "".join(s)