#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #list for num of reps index = num - 1  value = # of reps
        repHori = [0] * 9
        repVert = [0] * 9
        rep3b3 = [0] * 9

        for i in range(9):
            for k in range(9):
                if(board[i][k] != "."):
                    if(repHori[int(board[i][k])-1]==1):
                        return False
                    repHori[int(board[i][k])-1]=1
                
                if(board[k][i] != "."):
                    if(repVert[int(board[k][i])-1]==1):
                        return False
                    repVert[int(board[k][i])-1]=1
            
            repHori = [0]*9
            repVert = [0]*9
        
        for i in range(0,9,3):
            for k in range(0,9,3):
               for j in range(3):
                   for p in range(3):
                        if(board[i+j][k+p] != "."):
                            if rep3b3[int(board[i+j][k+p])-1] == 1:
                                return False
                            else:
                                rep3b3[int(board[i+j][k+p])-1] = 1
               rep3b3 = [0] * 9

        return True



# @lc code=end
