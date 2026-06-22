class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c=Counter(text)
        count=0
        while True:
            for i in "balloon":
                if i not in c:
                    return count
                else:
                    c[i]-=1
                    if not c[i]:del c[i]
            count+=1    