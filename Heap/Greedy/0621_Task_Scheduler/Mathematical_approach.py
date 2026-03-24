class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash=Counter(tasks).values()
        highest_count=max(hash)
        count_max=list(hash).count(highest_count)
        return max(len(tasks),(highest_count-1)*(n+1)+count_max)