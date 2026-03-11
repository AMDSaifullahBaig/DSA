class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return None
        dummy=ListNode(0,head)
        slow=dummy
        fast=head
        while fast.next and fast.next.next:
        	slow=slow.next
        	fast=fast.next.next
        if fast.next:slow=slow.next
        slow.next=slow.next.next
        return dummy.next