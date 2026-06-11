class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        node.next=head
        head=node
        prev=node
        while node.next and node.next.next:
            prev.next=node.next
            node.next.next=node
            prev=node
            node=node.next
        return head