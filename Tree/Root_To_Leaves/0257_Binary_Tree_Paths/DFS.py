class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        path=[]
        def traverse(node):
            if not node:return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                traverse(node.left)
                traverse(node.right)
            path.pop()
        traverse(root)        
        return result