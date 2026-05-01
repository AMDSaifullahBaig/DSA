class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        add=sum(nums)
        new_add=0
        for idx,val in enumerate(nums):
        	new_add+=idx*val
        maximum=new_add
        for i in range(1,n):
        	new_add=add+new_add
        	new_add-=n*nums[n-i]
        	maximum=max(maximum,new_add)
        return maximum