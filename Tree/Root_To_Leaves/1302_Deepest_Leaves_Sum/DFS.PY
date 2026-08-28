class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        add=0
        level=0
        maxlevel=0
        def dfs(root,level,maxlevel,add):
            if not root:return (level,maxlevel,add)
            level+=1
            if level>maxlevel:
                maxlevel=level
                add=0
            if maxlevel==level:
                add+=root.val
                print(add)
            _,maxlevel,add=dfs(root.left,level,maxlevel,add)
            _,maxlevel,add=dfs(root.right,level,maxlevel,add)
            return (level,maxlevel,add)
        level,maxlevel,add=dfs(root,level,maxlevel,add)
        return add