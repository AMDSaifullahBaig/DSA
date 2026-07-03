class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        symbol="*-+/"
        for i in tokens:
            if i in symbol:
                a=s.pop()
                b=s.pop()
                if i=="+":
                    s.append(a+b)
                if i=="-":
                    s.append(b-a)
                if i=="*":
                    s.append(a*b)
                if i=="/":
                    s.append(int(b/a))
            else:
                s.append(int(i))
        return s[0]