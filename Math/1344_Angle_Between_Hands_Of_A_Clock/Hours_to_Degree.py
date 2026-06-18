class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
    	delta=hour+minutes/60
    	delta=(delta*11)%12
    	return min(delta,12-delta)*30