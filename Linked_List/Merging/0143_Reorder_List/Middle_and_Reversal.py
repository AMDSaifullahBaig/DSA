class Solution:    	
    def reorderList(self, head: Optional[ListNode]) -> None:
    	if not head or not head.next or not head.next.next:return
    	fast=head
    	slow=head
    	while fast.next and fast.next.next:
    		fast=fast.next.next
    		slow=slow.next
    	curr=slow.next
    	slow.next=None
    	prev=None
    	while curr:
    		nxt=curr.next
    		curr.next=prev
    		prev=curr
    		curr=nxt
    	first=head
    	second=prev
    	while first and second:
    		temp1=first.next
    		temp2=second.next
    		first.next=second
    		second.next=temp1
    		second=temp2
    		first=temp1