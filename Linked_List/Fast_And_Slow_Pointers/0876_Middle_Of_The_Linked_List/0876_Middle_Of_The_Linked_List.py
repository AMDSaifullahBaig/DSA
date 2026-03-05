class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        while fast and fast.next:
        	fast=fast.next.next
        	head=head.next
        return head