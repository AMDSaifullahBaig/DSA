class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums))==len(nums):
            return False
        if len(nums)<=k+1:
            return True
        hash={}
        for idx,value in enumerate (nums):
            if value in hash and abs(hash[value]-idx)<=k:
                    return True
            hash[value]=idx
        return False