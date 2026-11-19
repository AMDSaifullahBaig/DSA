class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:return n
        current=0
        prev=2
        prev1=1
        for i in range(3,n+1):
            current=prev+prev1
            prev1=prev
            prev=current
        return current