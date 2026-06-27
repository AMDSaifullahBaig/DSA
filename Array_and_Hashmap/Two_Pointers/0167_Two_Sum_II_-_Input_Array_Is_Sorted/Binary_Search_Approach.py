class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            start=i+1
            end=n-1
            comp=target-numbers[i]
            first=i
            while start<=end:
                m=(start+end)//2
                if numbers[m]==comp:
                    return [first+1,m+1]
                elif numbers[m]<comp:
                    start=m+1
                else:
                    end=m-1