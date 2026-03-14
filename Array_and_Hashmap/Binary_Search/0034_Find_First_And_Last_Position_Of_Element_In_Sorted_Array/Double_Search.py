class Solution:
    def search(self,l,r,target,step,nums):
        idx=-1
        while l<=r:
            middle=(l+r)//2
            if target==nums[middle]:
            	idx=middle
            	if step:
            		r=middle-1
            	else:
            		l=middle+1
            elif target<nums[middle]:
            	r=middle-1
            else:
            	l=middle+1
       return idx
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        f=self.search(l,r,target,True,nums) 
        s=self.search(l,r,target,False,nums)
        return [f,s]