class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n&1:return False
        stack=[]
        for i in range(n):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top=stack.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return not stack