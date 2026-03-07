class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	if not head:
    		return None
    	if not head.next:
    		return head
    	curr=head
    	prev=None
    	while curr:
    		next=curr.next
    		curr.next=prev
    		prev=curr
    		curr=next
    	return prev