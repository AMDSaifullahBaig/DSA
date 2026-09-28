class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash={None:None}
        curr=head
        while curr:
            hash[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            hash[curr].next=hash[curr.next]
            hash[curr].random=hash[curr.random]
            curr=curr.next
        return hash[head]