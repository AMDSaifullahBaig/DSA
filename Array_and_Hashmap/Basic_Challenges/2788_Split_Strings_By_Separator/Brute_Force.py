class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        results=[]
        for i in words:
            if i=="":
                continue
            word=""
            for j in i:
                if j!=separator:
                    word+=j
                else:
                    if word!="":
                        results.append(word)
                    word=""
            if word!="":
                results.append(word)
        return results
        