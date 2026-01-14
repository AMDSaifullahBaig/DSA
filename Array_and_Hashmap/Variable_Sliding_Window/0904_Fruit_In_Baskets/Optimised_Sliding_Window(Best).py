class Solution:
    def totalFruit(self,fruits: List[int]) -> int:
        maximum=max(fruits)
        count=[0]*maximum
        result=0
        l=0
        unique=0
        for r in range (len(fruits)):
            if count[fruits[r]]==0:
                unique+=1
            count[fruits[r]]+=1
            while unique>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    unique-=1
                    l+=1
                if l-r+1>result:
                    result=r-l+1
        return result