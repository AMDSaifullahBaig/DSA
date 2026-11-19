class Solution:
    def dp(self,n,hash):
        if n<=1:
            return n
        if n==2:return 1
        if n in hash:
            return hash[n]
        hash[n]=self.dp(n-1,hash)+self.dp(n-2,hash)+self.dp(n-3,hash)
        return hash[n]
    def tribonacci(self, n: int) -> int:
        return self.dp(n,{})