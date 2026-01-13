class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=len(nums)
        prefix=[0]*(length+1)
        minimum=float("inf")
        for i in range(length):
            prefix[i+1]+=prefix[i]+nums[i]
        for i in range(length):
            l=i+1
            r=length
            complement=target+prefix[i]
            found=-1
            while l<=r:
                middle=(l+r)//2
                if prefix[middle]>=complement:
                    r=middle-1
                    found=middle
                else:
                    l=middle+1
            if found!=-1:
                minimum=min(minimum,found-i)
        return 0 if minimum==float("inf") else minimum