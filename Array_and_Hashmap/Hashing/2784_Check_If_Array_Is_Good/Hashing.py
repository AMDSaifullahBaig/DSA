class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        arr=[0]*n
        for i in nums:
            if i>=n:return False
            if arr[i]>0 and i<n-1:
                return False
            elif arr[i]>1 and i==n-1:
                return False
            arr[i]+=1
        return True