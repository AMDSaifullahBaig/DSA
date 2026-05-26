class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        word=set(word)
        for i in word:
            if i.islower():
                if i.upper() in word:
                    c+=1
        return c