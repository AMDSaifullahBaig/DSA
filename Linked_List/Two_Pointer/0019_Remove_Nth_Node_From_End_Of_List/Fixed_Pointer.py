class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:return 
        right=head
        left=head
        prev=None
        for i in range(n):
        	right=right.next
        if right==None:
        	return head.next
        while right:
        	right=right.next
        	
        	prev=left
        	left=left.next
        prev.next=left.next
        return head