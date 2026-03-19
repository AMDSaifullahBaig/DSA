class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter=Counter(words)
        result=sorted(counter.keys(),key=lambda x:(counter[x],x))
        return result[:k]