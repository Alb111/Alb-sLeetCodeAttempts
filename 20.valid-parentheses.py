#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        paraMap = {
            "(":")",
            "{":"}",
            "[":"]",
        }

        leftParaStack = []
        
        for char in s:
            if char in paraMap:
                leftParaStack.append(char)
            else:
                if(len(leftParaStack) == 0):
                    return False
                elif(paraMap[leftParaStack[-1]] == char):
                    leftParaStack.pop()
                else:
                    return False
                
        if (len(leftParaStack) == 0):
            return True





    

        
# @lc code=end

