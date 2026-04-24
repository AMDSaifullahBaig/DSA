class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d=0
        c=0
        for i in moves:
        	if i=="L":
        		d-=1
        	elif i=="R":
        		d+=1
        	else:
        		c+=1
        return max(abs(d+c),abs(d-c))