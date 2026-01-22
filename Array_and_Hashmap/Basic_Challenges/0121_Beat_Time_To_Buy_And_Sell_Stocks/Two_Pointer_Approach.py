class Solution(object):
    def maxProfit(self, prices):
        if not prices:
        	return 0
        min_price=float('inf')
        max_profit=0
        for i in prices:
            if i-min_price>max_profit:
                max_profit=i-min_price
            if i<min_price:
                min_price=i
        return max_profit