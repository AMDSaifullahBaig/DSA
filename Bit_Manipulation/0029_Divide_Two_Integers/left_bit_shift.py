class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        maximum=2**31-1
        minimum=-2**31
        sign=(dividend<0)^(divisor<0)
        if divisor==0:return maximum
        if dividend==minimum and divisor==-1:return maximum
        dividend=abs(dividend)
        divisor=abs(divisor)
        q=0
        while dividend>=divisor:
            temp=divisor
            multiple=1
            while dividend>=temp<<1:
                temp<<=1
                multiple<<=1
            dividend-=temp
            q+=multiple
        return -q*sign if sign else q