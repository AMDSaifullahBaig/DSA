class Solution:
    def canWinNim(self, n: int) -> bool:
        if n<=3: return True
        n%=4
        return True if n>0 and n<=3 else False