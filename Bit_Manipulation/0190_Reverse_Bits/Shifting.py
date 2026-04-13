class Solution:
    def reverseBits(self, n: int) -> int:
        remainder=0
        for i in range(32):
            remainder=remainder<<1|n&1
            n>>=1
        return remainder