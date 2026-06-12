class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor=0
        for i in s+t:
            xor^=ord(i)
        return chr(xor)