class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        end=goal[0]
        for i in range(len(s)):
            if  s[i]==end and s[i:]+s[:i]==goal:
            	return True
        return False