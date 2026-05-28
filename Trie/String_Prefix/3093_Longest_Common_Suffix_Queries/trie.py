class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = float('inf')

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int, wordsContainer: list[str]):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
            curr_best_idx = node.idx
            if curr_best_idx == float('inf'):
                node.idx = index
            elif len(wordsContainer[index]) < len(wordsContainer[curr_best_idx]):
                node.idx = index
            elif len(wordsContainer[index]) == len(wordsContainer[curr_best_idx]):
                if index < curr_best_idx:
                    node.idx = index

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        trie = Trie()
        best_default_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[best_default_idx]):
                best_default_idx = i
        trie.root.idx = best_default_idx
        
        for i, word in enumerate(wordsContainer):
            trie.insert(word[::-1], i, wordsContainer)
            
        ans = []
        for query in wordsQuery:
            node = trie.root
            for ch in query[::-1]:
                if ch in node.children:
                    node = node.children[ch]
                else:
                    break
            ans.append(node.idx)
        return ans