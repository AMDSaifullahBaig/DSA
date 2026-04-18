class Solution:
    def mirrorDistance(self, n: int) -> int:
        num=n
        result=0
        while num:
            result=(result*10)+(num%10)
            num//=10
        return abs(n-result)