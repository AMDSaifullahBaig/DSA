class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        maximum=-1
        result=[0]*n
        for i in range(n-2,-1,-1):
            if arr[i+1]>maximum:
                maximum=arr[i+1]
            result[i]=maximum
        result[-1]=-1
        return result