from typing import Dict, Tuple, Set, List

class Node:
    def __init__(self, char: str = "dummy") -> None:
        self.char: str = char
        self.leaves: Dict[str, Node] = {}

class Solution:
    def __init__(self) -> None:
        self.tree: Node = Node()
        self.board_size_x: int = 0
        self.board_size_y: int = 0
        self.used_pos: Set[Tuple[int, int]] = set()

    def find_pos_directions(self, pos) -> List[Tuple[int, int]]:
        output: List[Tuple[int, int]] = []

        # Check both x dir
        if (pos[0] + 1 < self.board_size_x) and ((pos[0] + 1, pos[1]) not in self.used_pos):
            output.append((pos[0] + 1, pos[1]))
        if (pos[0] - 1 > -1) and ((pos[0] - 1, pos[1]) not in self.used_pos):
            output.append((pos[0] - 1, pos[1]))

        # Check both y dir
        if (pos[1] + 1 < self.board_size_y) and ((pos[0], pos[1] + 1) not in self.used_pos):
            output.append((pos[0], pos[1] + 1))
        if (pos[1] - 1 > -1) and ((pos[0], pos[1] - 1) not in self.used_pos):
            output.append((pos[0], pos[1] - 1))

        return output


    def build_sub_tree(self, board: List[List[str]], cur_pos: Tuple[int, int], curr_iter: int, max_iter: int, dummy: Node) -> None:
        if curr_iter == max_iter:
            return

        pos_directions: List[Tuple[int, int]] = self.find_pos_directions(cur_pos)
        for direction in pos_directions:
            self.used_pos.add(direction)
            if board[direction[0]][direction[1]] not in dummy.leaves:
                dummy.leaves[board[direction[0]][direction[1]]] = Node(board[direction[0]][direction[1]])
            self.build_sub_tree(board, direction, curr_iter + 1, max_iter, dummy.leaves[board[direction[0]][direction[1]]])
            self.used_pos.remove(direction) # not sure

    def build_tree(self, board: List[List[str]], max_len: int) -> None:
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.used_pos = set()
                self.used_pos.add((row, col))

                if board[row][col] not in self.tree.leaves:
                    start_node: Node = Node(board[row][col])
                    self.tree.leaves[board[row][col]] = start_node

                self.build_sub_tree(board, (row, col), 0, max_len, self.tree.leaves[board[row][col]])


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        output: List[str] = []
        max_len: int = max(len(word) for word in words)
        self.board_size_y = len(board)
        self.board_size_x = len(board[0])

        
        self.build_tree(board, max_len)

        for word in words:
            dummy: Node = self.tree
            for char in word:
                if char not in dummy.leaves:
                    break
                dummy = dummy.leaves[char]
            else:
                output.append(word)

        return output

