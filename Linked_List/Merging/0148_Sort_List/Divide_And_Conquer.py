class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if not head or not head.next:
       	return head
       fast=head
       slow=head
       while fast.next and fast.next.next:
       	slow=slow.next
       	fast=fast.next.next
       middle=slow.next
       slow.next=None
       l=self.sortList(head)
       r=self.sortList(middle)
       return self.merge(l,r)
    def merge(self,p1,p2):
       	dummy=ListNode()
       	p=dummy
       	while p1 and p2:
       		if p1.val<p2.val:
       			p.next=p1
       			p1=p1.next
       			p=p.next
       		else:
       			p.next=p2
       			p2=p2.next
       			p=p.next
       	p.next=p1 or p2
       	return dummy.next