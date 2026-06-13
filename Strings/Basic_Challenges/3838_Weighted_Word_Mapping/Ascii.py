class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result=[]
        for i in words:
            summation=0
            for j in i:
                summation+=weights[ord(j)-97]
            result.append(chr(122-(summation%26)))
        return "".join(result)