
def search(trie):
    result=[]
    
    for key in trie:
        if key=="END":
            result.append(trie["END"])
        else:
            result+=search(trie[key])
    return result

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}
        
        for word in products:
            currentPos = trie
            for letter in word:
                if letter not in currentPos:
                    currentPos[letter]={}
                currentPos=currentPos[letter]
            currentPos["END"]=word
        
        currentPos = trie
        result=[[] for _ in range(len(searchWord))]
        i=0
        for letter in searchWord:
            if letter not in currentPos:
                break
            else:
                currentPos = currentPos[letter]
                result[i]=search(currentPos)
                i+=1
        for i in range(len(result)):
            result[i].sort()
            if len(result[i])>3:
                result[i]=result[i][:3]
        return result
            
        
