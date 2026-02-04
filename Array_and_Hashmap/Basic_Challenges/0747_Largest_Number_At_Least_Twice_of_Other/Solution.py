class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum1=0
        idx=-1
        maximum2=0
        for i in range(len(nums)):
            if nums[i]>maximum1:
                maximum2=maximum1
                maximum1=nums[i]
                idx=i
            elif nums[i]>maximum2:
                maximum2=nums[i]
        return idx if (maximum1)>=(maximum2*2) else -1