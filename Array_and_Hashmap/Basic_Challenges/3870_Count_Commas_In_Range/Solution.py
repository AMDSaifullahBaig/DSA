class Solution:
    def countCommas(self, n: int) -> int:
        curr=0
        limit=1000
        while n>=limit:
            curr+=n-limit+1
            limit*=1000
        return curr