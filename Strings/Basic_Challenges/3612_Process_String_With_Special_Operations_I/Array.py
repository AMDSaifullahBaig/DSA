class Solution:
    def processStr(self, s: str) -> str:
        arr=[]
        for i in s:
            if i.isalpha():
                arr.append(i)
            elif i=="#":
                arr*=2
            elif i=="*" and arr:
                arr.pop()
            elif i=="%":
                arr.reverse()
        return "".join(arr)