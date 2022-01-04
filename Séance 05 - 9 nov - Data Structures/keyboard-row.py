class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")
        
        rep=[]
        
        for word in words:
            candidat = set(word.lower())
            if candidat.issubset(row1) or candidat.issubset(row2) or candidat.issubset(row3):
                rep.append(word)
        return(rep)
                
