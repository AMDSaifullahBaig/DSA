class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)&1==1:return False
        stack=[s[0]]
        hash={"]":"[",")":"(","}":"{"}
        for i in s[1:]:
            if i in hash and stack and stack[-1]==hash[i]:
                stack.pop()
            else:
                stack.append(i)
        return not stack