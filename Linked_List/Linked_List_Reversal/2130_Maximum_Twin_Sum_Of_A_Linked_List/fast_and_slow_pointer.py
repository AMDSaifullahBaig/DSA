class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            next=slow.next
            slow.next=prev
            prev=slow
            slow=next
        maximum=0
        while prev and slow:
            maximum=max(maximum,prev.val+slow.val)
            slow=slow.next
            prev=prev.next
        return maximum