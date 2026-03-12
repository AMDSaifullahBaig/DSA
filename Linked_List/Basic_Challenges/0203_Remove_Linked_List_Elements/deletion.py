class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        p=head
        while p.next:
        	if p.next.val==val:
        		p.next=p.next.next
        	else:
        		p=p.next
        return dummy.next