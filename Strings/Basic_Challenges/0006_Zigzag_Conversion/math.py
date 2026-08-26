class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:return s
        level=[[] for i in range(numRows)]
        n=len(s)
        c=0
        while c<n:
            if c<n and c+numRows<=n:
                k=numRows
            else:
                k=n-c
            for i in range(k):
                level[i].append(s[c])
                c+=1
            if c<n:
                idx=numRows-2
                if n-c<numRows-2:
                    k=n-c
                else:
                    k=numRows-2
                for i in range(k):
                    level[idx].append(s[c])
                    idx-=1
                    c+=1
        for i in range(len(level)):
            level[i]="".join(level[i])
        return "".join(level)