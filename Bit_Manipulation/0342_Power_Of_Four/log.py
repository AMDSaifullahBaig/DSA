class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:return False
        if n<0:n*=-1
        return log(n,4).is_integer()