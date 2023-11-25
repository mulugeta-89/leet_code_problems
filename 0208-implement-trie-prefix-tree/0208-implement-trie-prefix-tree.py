class Trienode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Trienode()
    def insert(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = Trienode()
            curr_node = curr_node.children[letter]
        curr_node.isEnd = True
    def search(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.isEnd
    def startsWith(self, prefix):
        curr_node = self.root
        flag = True
        for letter in prefix:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return flag