class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result=[]
        for word in queries:
        	for i in dictionary:
        		count=0
        		for j in range(len(word)):
        			if word[j]!=i[j]:
        				count+=1
        		if count<=2:
        			result.append(i)
        			break
        return result