class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n=len(s)
        a,pre=[0]*n,[0]*n
        a[0]=1
        for i in range(minJump):
            pre[i]=1
        for i in range(minJump, n):
            left,right=i-maxJump,i-minJump
            if s[i]=="0":
                total=pre[right]-(0 if left<=0 else pre[left-1])
                a[i]=int(total!=0)
            pre[i]=pre[i-1]+a[i]
        return bool(a[n-1])