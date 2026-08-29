class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if s=="":return 0
        sign=1
        result=0
        start=0
        if s[0]=="+" or s[0]=="-":
            if s[0]=="-":
                sign=-1
            start=1
        for i in s[start:]:
            if i=="  ":
                print("space")
                continue
            elif 48<=ord(i)<=57:
                result=result*10+int(i)
            else:
                break
        if sign<0:
            return max((1<<31)*-1,result*sign)
        return min((1<<31)-1,result)