class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:return False
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            head=head.next
            if head==fast:
                return True
        return False