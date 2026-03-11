from typing import Dict, Set

class PrefixTreeNode:
    def __init__(self, char_to_insert: str) -> None:
        self.char: str =  char_to_insert
        self.end_of_word: bool = False
        self.leaves: Dict[str, PrefixTreeNode] = {} 

class PrefixTree:

    def __init__(self) -> None:
        self.head_node: PrefixTreeNode = PrefixTreeNode("dummy")

    def insert(self, word: str) -> None:
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

        dummy_node.end_of_word = True

    def search(self, word: str) -> bool:
        dummy_node: PrefixTreeNode = self.head_node
        for char in word:
            print(dummy_node.char)
            if char in dummy_node.leaves:
                # go into that leaf
                dummy_node = dummy_node.leaves[char]
            else:
                # pattern not found
                return False

        return dummy_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        # parse tree
        dummy_node: PrefixTreeNode = self.head_node
        for char in prefix:
            if char in dummy_node.leaves:
                # go into that leaf
                dummy_node = dummy_node.leaves[char]
            else:
                # pattern not found
                return False
        # all pattern was found
        return True
