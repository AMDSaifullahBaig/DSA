class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash=set()
        n=len(nums)
        slow=0
        for i in range(n):
            if nums[i] not in hash:
                hash.add(nums[i])
                nums[slow]=nums[i]
                slow+=1
        return slow