class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        rep = []
        candidates = {"(":n,")":0}
        
        def addNewChar(string : str, candidates):
            if candidates["("]+candidates[")"]==0:
                rep.append(string)
                return
            
            if candidates["("]:
                candidates["("]-=1
                candidates[")"]+=1
                addNewChar(string+"(",candidates)
                candidates["("]+=1
                candidates[")"]-=1
            
            if candidates[")"]:
                candidates[")"]-=1
                addNewChar(string+")",candidates)
                candidates[")"]+=1
            return
            
            
        addNewChar("",candidates)     
        
        return rep
