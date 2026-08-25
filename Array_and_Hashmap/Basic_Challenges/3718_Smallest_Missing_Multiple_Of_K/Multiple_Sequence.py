class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        maximum=max(nums)
        print(maximum)
        for i in range(k,maximum,k):
            if i not in nums:
                return i
        if maximum%k==0:
            return maximum+k
        else:
            return (maximum//k)*k+k