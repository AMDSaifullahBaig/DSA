class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
    	s_len=len(s)
    	p_len=len(p)
    	if p_len>s_len:
    		return []
    	p_count=[0]*26
    	s_count=[0]*26
    	results=[]
    	for i in range(p_len):
    	   p_count[ord(p[i])-ord('a')]+=1
    	   s_count[ord(s[i])-ord('a')]+=1
    	if p_count==s_count:results.append(0)
    	for i in range(p_len, s_len):
    	    s_count[ord(s[i])-ord('a')]+=1
    	    s_count[ord(s[i-p_len])-ord('a')]-=1
    	    if s_count==p_count:
    	    	results.append(i-p_len+1)
    	return results