class Node:
    
    def __init__(self,content):
        self.children={}
        self.word=False
        self.content=content
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start=Node('/')
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pos=self.start
        for car in word:
            if car not in pos.children:
                pos.children[car]=Node(car)
            
            pos=pos.children[car]
        pos.word=True
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pos=self.start
        for car in word:
            if car not in pos.children:
                return False
            pos=pos.children[car]
        if pos.word:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pos=self.start
        for car in prefix:
            if car not in pos.children:
                return False
            pos=pos.children[car]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
