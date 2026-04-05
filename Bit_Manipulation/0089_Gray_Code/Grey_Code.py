class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [int(str(i^(i>>1)),10) for i in range(2**n)]