class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        s=list(s)
        v=set("aeiouAEIOU")
        l,r=0,n-1
        while l<r:
        	while l<r and s[l] not in v:
        		l+=1
        	while l<r and s[r] not in v:
        		r-=1
        	s[l],s[r]=s[r],s[l]
        	l+=1
        	r-=1
        return "".join(s)