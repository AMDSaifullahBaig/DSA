class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n=len(strs)
        limit=0
        f,l=strs[0],strs[-1]
        while len(f)>limit and len(l)>limit and f[limit]==l[limit] :
        	limit+=1
        return strs[0][:limit]