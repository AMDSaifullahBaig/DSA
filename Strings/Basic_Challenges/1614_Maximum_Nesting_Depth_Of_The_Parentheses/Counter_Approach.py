class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        depth=0
        maximum=0
        for i in s:
        	if i=="(":
        		depth+=1
        		maximum=max(depth,maximum)
        	elif i==")":
        		depth-=1
        return depth