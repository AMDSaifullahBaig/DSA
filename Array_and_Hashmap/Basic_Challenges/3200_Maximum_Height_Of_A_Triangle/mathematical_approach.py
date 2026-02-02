class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
    	def rows(n1,n2):
    		odd=int(math.sqrt(n1))
    		even=int((-1+math.sqrt(1+4*n2))//2)
    		if odd>even:
    			return even*2+1
    		return odd*2
    	return max(rows(blue,red),rows(red,blue))