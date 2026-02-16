class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1],[1,1]]
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return result
        for i in range(1,numRows-1):
            prev=result[i]
            result2=[1]
            for i in range(1,len(prev)):
                result2.append(prev[i-1]+prev[i])
            result2.append(1)
            result.append(result2)
        return result