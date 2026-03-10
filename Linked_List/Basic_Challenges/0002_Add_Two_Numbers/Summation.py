class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0)
        head=dummy
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            value=v1+v2+carry
            ones=value%10
            carry=value//10
            head.next=ListNode(ones)
            head=head.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next