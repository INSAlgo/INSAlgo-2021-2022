from itertools import permutations

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        rep=[]
     
        for word in words:
            dico={}
            for i in range(len(pattern)):
                if pattern[i] not in dico:
                    if word[i] in dico.values():
                        break
                    else:
                        dico[pattern[i]]=word[i]
                else:
                    if dico[pattern[i]]!=word[i]:
                        break
            else:
                rep.append(word)
        return(rep)
