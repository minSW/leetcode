import collections

class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word :
            node = node.children[w]
        node.end = True
        
    def search(self, word: str) -> bool:
        def dfs(node, path) :
            res = False
            
            if not path :
                res = node.end
            elif path[0] == "." :
                for ch in node.children.values() :
                    res = res or dfs(ch, path[1:])
                    if res : break
            elif path[0] in node.children :
                res = res or dfs(node.children[path[0]], path[1:])
            
            return res

        return dfs(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
