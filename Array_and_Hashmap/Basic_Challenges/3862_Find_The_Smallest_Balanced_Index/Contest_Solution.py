class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        l=0
        r=len(nums)-1
        a=0
        p=1
        while l<r:
            if a<p:
                a+=nums[l]
                l+=1
            else:
                p*=nums[r]
                r-=1
            if a==p and l-r==0:
                return l
        return -1