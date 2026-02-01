class Solution(object):
    def splitWordsBySeparator(self, words, separator):
    	result=[]
    	for word in words:
    		removed=word.split(separator)
    		result.extend(removed)
    	answer=[]
    	for solution in result:
    		if solution!="":
    			answer.append(solution)
    	return answer