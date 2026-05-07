class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
    	stack=[]
    	result=[0]*len(nums)
    	for i in range(len(nums)):
    		maximum=nums[i]
    		minimum=nums[i]
    		left=i
    		right=i
    		while stack and minimum<stack[-1][0]:
    			prev_maximum,prev_minimum,l,r=stack.pop()
    			maximum=max(maximum,prev_maximum)
    			minimum=min(minimum,prev_minimum)
    			left=l
    		stack.append((maximum,minimum,curr,left,right))
    	for i in range(len(stack)):
    		for j in range(stack[i][2],stack[i][3]+1):
    			result[j]=stack[i][0]
    	return result