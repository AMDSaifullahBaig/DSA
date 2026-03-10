class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	if not head:
    		return 
    	if not head.next:
    		return head
    	e=head.next
    	o=head
    	even_head=e
    	while e and e.next:
    		o.next=e.next
    		o=o.next
    		e.next=o.next
    		e=e.next
    	o.next=even_head
    	return head