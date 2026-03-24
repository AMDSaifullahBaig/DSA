class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts=Counter(tasks)
        heap=[-i for i in counts.values()]
        heapq.heapify(heap)
        c=0
        queue=deque()
        while heap or queue:
            c+=1
            if heap
                count=heapq.heappop(heap)+1
                if cnt!=0:
                    queue.append((count,c+n))
            if queue and queue[0][1]==c
                heapq.heappush(heap,queue.popleft()[0])
        return c