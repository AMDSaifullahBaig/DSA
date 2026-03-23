class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    	if not lists:return
    	dummy=ListNode(0)
    	curr=dummy
    	heap=[]
    	for idx,node in enumerate(lists):
            if node:heappush(heap,(node.val,idx,node))
    	while heap:
    		val,idx,node=heappop(heap)
    		curr.next=node
    		curr=curr.next
    		if node.next:
    			heappush(heap,(node.next.val,idx,node.next))
    	return dummy.next