class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        minimum=float('inf')
        idx=-1
        for i in range(len(capacity)):
            if capacity[i]>=itemSize and capacity[i]<minimum:
                    minimum=capacity[i]
                    idx=i
        return idx