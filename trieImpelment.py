class Trie:
    class TrieNode:
        # isEnd = False
        # children = []*26
        def __init__(self):
            self.children= [0]*26
            self.isEnd= False
 
    
    # root     = TrieNode( )    
    def __init__(self):
        self.root = self.TrieNode( ) 
    
    # TC:#O(L)
    #SC O(nk): n no of words, k is avg lenghth of word

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if cur.children[ord(i)-ord('a')] == 0:
                cur.children[ord(i)-ord('a')] = self.TrieNode()
            cur = cur.children[ord(i)-ord('a')]
        cur.isEnd = True
    
    # TC:#O(L)

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if cur.children[ord(i)-ord('a')] == 0:
                return False
            cur =  cur.children[ord(i)-ord('a')]
        return cur.isEnd 
    # TC:#O(L)

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if cur.children[ord(i)-ord('a')] == 0:
                return False
            cur =  cur.children[ord(i)-ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
