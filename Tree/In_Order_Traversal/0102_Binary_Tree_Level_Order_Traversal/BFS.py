class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result=[]
        queue=deque([root])
        while queue:
            curr=[]
            for i in range(len(queue)): 
                e=queue.popleft()
                curr.append(e.val)
                if e.left: 
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            result.append(curr)
        return result