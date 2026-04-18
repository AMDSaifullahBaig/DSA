class Solution:
  def calculate(self, s: str) -> int:
  	num=0
  	result=0
  	sign=1
  	stack=[]
  	for i in s:
  		if i.isdigit():
  			num=num*10+int(i)
  		elif i=="(":
  			stack.append(sign)
  		elif i==")":
  			stack.pop()
  		elif i=="+" or i=="-":
  			result+=num*sign
  			sign=(1 if i=="+" else -1)*stack[-1]
  			num=0
  		return result+sign*num  			