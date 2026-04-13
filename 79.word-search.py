from typing import List, Tuple, Set
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def find_chocies(x_index: int, y_index: int, x_size: int, y_size: int) -> List[Tuple[int, int]]:
            chocies: List[Tuple[int, int]] = []

            # find all possible paths           
            # left
            if x_index - 1 >= 0:
                chocies.append((x_index - 1, y_index))
            # right
            if x_index + 1 < x_size:
                chocies.append((x_index + 1, y_index))
            # up
            if y_index - 1 >= 0:
                chocies.append((x_index, y_index - 1))
            # down
            if y_index + 1 < y_size:
                chocies.append((x_index, y_index + 1))

            return chocies


        def try_to_find_word(word_index: int, cords: Tuple[int, int], used_cords: Set[Tuple[int, int]]) -> bool:

            # base case
            if word_index == len(word):
                # this gets hit but my function returns False for some reasion
                return True

            choices: List[Tuple[int, int]] = find_chocies(cords[0], cords[1], x_size, y_size)
            for choice in choices:
                if board[choice[1]][choice[0]] == word[word_index] and choice not in used_cords:
                    used_cords.add(choice)
                    if try_to_find_word(word_index + 1, choice, used_cords): 
                        return True
                    used_cords.remove(choice)

            return False

        x_size: int = len(board[0])
        y_size: int = len(board)
        used: Set[Tuple[int, int]] = set()
        # go through and find the first char
                
        for x in range(x_size):
            for y in range(y_size):
                if board[y][x] == word[0]:
                    used.add((x,y))
                    if try_to_find_word(1, (x, y), used):
                        return True
                    used.remove((x,y))

        return False


board=[["A","B","C","D"],["S","A","A","T"],["A","C","A","E"]]
word="CAT"

x = Solution()
print(x.exist(board, word))

                    
