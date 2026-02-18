class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter 
        count=Counter(words[0])
        for i in range(1,len(words)):
            count&=Counter(words[i])
        return list(count.elements())