class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        ops="+"
        s+="+"
        num=0
        for i in s:
        	if i.isdigit():
        		num=num*10+int(i)
        		continue
        	if i==" ":
        		continue
        	if ops=="+":
        			stack.append(num)
        	elif i=="-":
        		stack.append(-num)
        	elif i=="*":
        		stack.append(stack.pop()*num)
        	elif i=="/":
        		stack.append(int(stack.pop()/num))
        	ops=i
        	num=0
        return sum(stack)