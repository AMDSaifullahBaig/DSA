class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c=Counter(s)
        count=0
        while True:
            for i in target:
                if i not in c:
                    return count
                else:
                    c[i]-=1
                    if not c[i]:del c[i]
            count+=1