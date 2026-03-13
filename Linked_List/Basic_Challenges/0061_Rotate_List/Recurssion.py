class Solution:
    def rotation(self,p,n):
        if not n:
            return p
        head=p
        while head.next.next:
            head=head.next
        head.next.next=p
        p=head.next
        head.next=None
        n-=1
        return self.rotation(p,n)
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return
        if not head.next:
            return head
        c=0
        p=head
        while p:
            p=p.next
            c+=1
        k=k%c
        return self.rotation(head,k)