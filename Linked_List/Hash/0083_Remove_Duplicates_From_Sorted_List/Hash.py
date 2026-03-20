class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
        	return
        p=head
        hash=set()
        hash.add(head.val)
        while p.next:
        	if p.next.val not in hash:
        		hash.add(p.next.val)
        		p=p.next
        	else:
        		p.next=p.next.next
        return head