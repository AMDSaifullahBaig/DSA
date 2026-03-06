class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash=set()
        while head and head.next:
            if head in hash:
                return head
            hash.add(head)
            head=head.next