# program for implementing trie

class TrieNode:
    
    def __init__(self):
        self.children = [None]*26
        self.count = 0
        self.eow = False

class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    @staticmethod
    def char2index(ch):
        return ord(ch)-ord('a')

    def isempty(self, trav):
        for i in trav.children:
            if i == None:
                return True 
        return False

    def insert(self, key):
        trav = self.root 
        for ch in key:
            index = Trie.char2index(ch)
            if not trav.children[index]:
                trav.children[index] = self.get_node()
            trav = trav.children[index]
        trav.eow = True 

    def search(self, key):
        trav = self.root 
        for ch in key:
            index = Trie.char2index(ch)
            if not trav.children[index]:
                return False
            trav = trav.children[index]
        return trav!=None and trav.eow

    def remove(self, key, root, depth=0):
        
        # if key is not present do not modify the trie
        # key can be part of another long key. Just unmark end of word.
        # If last char of key does not have child boom
        # Check for childens if required for otherkeys.
        # if node does not have child + EOW is false Boom.

        trav = root
        # if root is null
        if trav == None:
            return trav

        # for last element
        if depth == len(key)-1:
            if trav.eow:
                trav.eow = False
            if self.isempty(trav):
                trav.children= None
                trav=None
            return trav

        # non last character 
        index = Trie.char2index(key[depth])
        trav.children[index] = self.remove(key, trav.children[index], depth+1)
        
        # empty + not end of word.. boom!
        if self.isempty(trav) and trav.eow == False:
            trav = None
        return trav


if __name__ == "__main__":
    t = Trie()
    t.insert("the")
    print(t.search("the"))
    t.remove("the", t.root)
    print(t.search("the"))


            

