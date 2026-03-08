class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
        	return True
        fast=head
        slow=head
        while fast.next and fast.next.next:
        	slow=slow.next
        	fast=fast.next.next
        curr=slow.next
        prev=None
        while curr:
        	next=curr.next
        	curr.next=prev
        	prev=curr
        	curr=next
        while prev:
        	if prev.val!=head.val:
        		return False
        	head=head.next
        	prev=prev.next
        return True