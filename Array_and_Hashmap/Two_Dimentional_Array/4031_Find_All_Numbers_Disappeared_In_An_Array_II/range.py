class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        result=[]
        start=lower
        nums=set(nums)
        for i in range(lower,upper+1):
            if i in nums:
                if start==i:
                    lower+=1
                else:
                    if start<=i-1:
                        result.append([start,i-1])
                start=i+1
        if start<=upper:
            result.append([start,upper])
        return result
a=Solution()
nums = [3,9,7]
lower = 1
upper = 12
print(a.findDisappearedNumbers(nums,lower,upper))