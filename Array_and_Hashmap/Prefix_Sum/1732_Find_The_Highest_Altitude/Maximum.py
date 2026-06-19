class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum=0
        curr=0
        for i in gain:
            curr+=i
            if curr>maximum:maximum=curr
        return maximum