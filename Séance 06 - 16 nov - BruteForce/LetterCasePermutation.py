class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result=set()
        result.add(S)
        for i in range(len(S)):
            current=set()
            for A in result:
                B=list(A)
                B.pop(i)
                B.insert(i,S[i].lower())
                current.add(''.join(B))
                B.pop(i)
                B.insert(i,S[i].upper())
                current.add(''.join(B))
            result=result.union(current)
        return result
