class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_s=len(s)
        len_r=len(s)
        if len_s!=len_r:
            return False
        hash_x={}
        hash_y={}
        for i in range(len_s):
            char_s=s[i]
            char_t=t[i]
            if char_s in hash_x:
            	if hash_x[char_s]!=char_t:
                    return False
            else:
                hash_x[char_s]=char_t
            if char_t in hash_y:
                if hash_y[char_t]!=char_s:
                    return False
            else:
                hash_y[char_t]=char_s
        return True