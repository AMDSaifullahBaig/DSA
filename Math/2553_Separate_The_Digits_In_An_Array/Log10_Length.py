class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
        	if i==0:
        		result.append(0)
        		continue
        	n=int(log10(i)+1)
        	for j in range(n-1,-1,-1):
        		digit=i//(10**j)
        		i%=10**j
        		result.append(digit)
        return result