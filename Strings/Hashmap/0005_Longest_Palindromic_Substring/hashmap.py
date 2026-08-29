class Solution:
    def longestPalindrome(self, s: str) -> str:
        hash={}
        maximum=0
        start=0
        end=0
        for idx,val in enumerate(s):
            if val not in hash:
                hash[val]=[idx]
            else:
                hash[val].append(idx)
        for idx,val in enumerate(s):
            for i in (hash[val][::-1]):
                if s[idx:i+1]==s[idx:1+i][::-1]:
                    if maximum<=i+1-idx:
                        maximum=i+1-idx
                        start=idx
                        end=i+1
                        break
        return s[start:end]