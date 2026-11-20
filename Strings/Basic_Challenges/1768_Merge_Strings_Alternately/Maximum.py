class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c1=len(word1)
        c2=len(word2)
        p1=p2=0
        maximum=max(c1,c2)
        arr=[]
        for i in range(maximum):
            if i<c1:
                arr.append(word1[i])
            if i<c2:
                arr.append(word2[i])
        return "".join(arr)