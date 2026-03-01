class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash={}
        l=0
        result=0
        for idx,val in enumerate(s):
            if val in hash and hash[val]>=l:
                l=hash[val]+1
            hash[val]=idx
            curr=idx-l+1
            if result<curr:
            	result=curr
        return result