class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:return None
        if head and left==right:
        	return head
        dummy=ListNode(0)
        dummy.next=head
        fixed=dummy
        for i in range(left-1):
        	fixed=fixed.next
        curr=fixed.next
        for i in range(right-left):
        	nxt=curr.next
        	curr.next=nxt.next
        	nxt.next=fixed.next
        	fixed.next=nxt
        return dummy.next