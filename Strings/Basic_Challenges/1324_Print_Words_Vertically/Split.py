class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split()
        result=[]
        maximum=max(len(word) for word in words)
        for i in range(maximum):
            curr=""
            for j in words:
                if i<len(j):
                    curr+=j[i]
                else:
                    curr+=" "
            result.append(curr.rstrip())
        return result