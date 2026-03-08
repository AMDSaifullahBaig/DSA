class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    	ptr1=headA
    	ptr2=headB
    	while ptr1!=ptr2:
    		ptr1=ptr1.next if ptr1 else headB
    		ptr2=ptr2.next if ptr2 else headA
    	return ptr1 