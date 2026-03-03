from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        rem=0
        result=0
        for i in c.values():
            result+=(i//2)*2
            if i%2==1:rem=1
        return result+rem