class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            middle=(l+r)//2
            if nums[middle]==target:return middle
            elif target>nums[middle]:
            	l=middle+1
            	continue
            elif target<nums[middle]:
            	r=middle-1
            	continue
       return -1