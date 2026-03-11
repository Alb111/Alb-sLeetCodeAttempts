from typing import Dict
class Node:
    def __init__(self) -> None:
        self.leaves: Dict[str, Node] = {}
        self.end_of_word: bool = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        dummy_node: Node = self.root

        for char in word:
            # if there is a node go to that one otherwise add it in 
            if char not in dummy_node.leaves:
                dummy_node.leaves[char] = Node()
            dummy_node = dummy_node.leaves[char]

        # set last node to end of word
        dummy_node.end_of_word = True


    def search_from_node(self, starting_node: Node, word: str) -> bool:
        dummy_node: Node = starting_node

        for index, char in enumerate(word):

            if char == ".":
                for node in dummy_node.leaves.values():
                    if self.search_from_node(node, word[index+1:]):
                        return True 

                return False
                    
            if char not in dummy_node.leaves:
                print(char)
                return False

            dummy_node = dummy_node.leaves[char]

        return dummy_node.end_of_word
    
    def search(self, word: str) -> bool:
        return self.search_from_node(self.root, word)

