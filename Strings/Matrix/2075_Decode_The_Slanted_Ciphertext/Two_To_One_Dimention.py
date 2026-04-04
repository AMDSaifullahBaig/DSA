class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        result=[]
        n=len(encodedText)
        col=n//rows
        for i in range(col):
        	x=i
        	y=0
        	while y<rows and x<col:
        		result.append(encodedText[(y*col)+x])
        		x+=1
        		y+=1
        return "".join(result).rstrip()