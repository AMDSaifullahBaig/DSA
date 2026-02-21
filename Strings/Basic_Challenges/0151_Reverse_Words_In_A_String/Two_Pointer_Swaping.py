class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        l=0
        r=len(s)-1
        while l<r:
            s[l],s[r]=s[r].strip(),s[l].strip()
            l+=1
            r-=1
        return " ".join(s)