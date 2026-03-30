class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even=Counter(s1[::2])
        for i in s2[::2]:
        	even[i]-=1
        odd=Counter(s1[1::2])
        for i in s2[1::2]:
        	odd[i]-=1
        return all(i==0 for i in even) and all(i==0 for i in odd)