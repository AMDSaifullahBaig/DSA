class Solution:
    def sumAndMultiply(self, n: int) -> int:
        add=0
        num=0
        c=0
        while n:
            digit=(n%10)
            if digit:
                num=num+digit*(10**c)
                c+=1
            add+=digit
            n//=10
        return num*add