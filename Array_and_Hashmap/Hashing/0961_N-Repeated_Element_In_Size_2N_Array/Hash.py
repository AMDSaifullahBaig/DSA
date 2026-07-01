class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash=set()
        for i in nums:
            if i not in hash:
                hash.add(i)
            else:
                return i