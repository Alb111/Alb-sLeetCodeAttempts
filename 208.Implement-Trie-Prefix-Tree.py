from typing import Dict, Set

class PrefixTreeNode:
    def __init__(self, char_to_insert: str) -> None:
        self.char: str =  char_to_insert
        self.leaves: Dict[str, PrefixTreeNode] = {} 

class PrefixTree:

    def __init__(self):
        self.head_node: PrefixTreeNode = PrefixTreeNode("dummy")
        self.words: Set = set()

    def insert(self, word: str) -> None:
        # track word
        self.words.add(word)

        # make/parse a tree
        dummy_node: PrefixTreeNode = self.head_node
        for char in word:
            if char in dummy_node.leaves:
                # go into that leaf
                dummy_node = dummy_node.leaves[char]
            else:
                # add it 2 the tree
                to_add: PrefixTreeNode = PrefixTreeNode(char) 
                dummy_node.leaves[char] = to_add 
                dummy_node = to_add

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        # parse tree
        dummy_node: PrefixTreeNode = self.head_node
        for char in prefix:
            print(dummy_node.char)
            if char in dummy_node.leaves:
                # go into that leaf
                dummy_node = dummy_node.leaves[char]
            else:
                # pattern not found
                return False
        # all pattern was found
        return True

x = PrefixTree()
x.insert("apple")
print(x.startsWith("app"))


