class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result=0
        while head:
            result+=head.val
            if head.next:
                result*=2
            head=head.next
        return result
        