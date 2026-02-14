class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)-1
        if k>n:
            k=k%(n+1)
        l,r=0,n
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l=0
        limit=k-1
        while l<limit:
            nums[l],nums[limit]=nums[limit],nums[l]
            l+=1
            limit-=1
        r=n
        limit=k
        while limit<r:
            nums[r],nums[limit]=nums[limit],nums[r]
            limit+=1
            r-=1