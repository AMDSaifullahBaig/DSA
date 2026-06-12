class Solution:
    def toHex(self, num: int) -> str:
        if num=="0":return "0"
        if num<0:num+=2**32
        hex="0123456789abcdef"
        result=[]
        while num:
            result.append(hex[num&15])
            num//=16
        return "".join(result)[::-1]