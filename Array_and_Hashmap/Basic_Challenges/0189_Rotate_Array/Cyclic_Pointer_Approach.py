class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        arr=[]
        for i in range(n):
            arr.append(nums[(n-k+i)%n])
        nums[:]=arr
        return nums