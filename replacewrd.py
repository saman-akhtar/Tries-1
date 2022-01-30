class Solution:
    #Tc O(NL) + O(L) n is no of words, L average length of word
    #Sc O(NL) + O(N) for stroing words
    class TrieNode:
        def __init__(self):
            self.child = [0]*26
            self.end = False
    def create(self,root,dic):
        
        for word in dic:
            cur = root
      
            for i in word:
                if cur.child[ord(i)-ord("a")] == 0:
                    cur.child[ord(i)-ord("a")] = self.TrieNode()
                cur = cur.child[ord(i)-ord("a")] 
            cur.end = True
        return root
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        if dictionary is None or len(dictionary )==0:
            return 0
        root = self.TrieNode()
       
        root = self.create(root,dictionary)
        def search(root, sent):
            txt = ""
            
            for word in sent:
                wrd = ""
                cur = root
                for i in word:
                    if cur.end == True or cur.child[ord(i)-ord("a")] == 0:
                        #flag = 0
                        break
                    else:
                        #flag = 1
                        wrd = wrd+ i
                        
                    cur = cur.child[ord(i)-ord("a")]
                if wrd == "" or cur.end == False:
                    txt = txt +  word + " "
                else:
                    txt = txt + wrd+ " "
            return txt.strip()
        sent = sentence.split(" ")
        return search (root, sent)
                    
            
            
