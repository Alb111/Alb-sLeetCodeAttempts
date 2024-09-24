#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def createDict(self, str):
        temp = {}
        for char in str:
            if char in temp:
                temp[char]+=1
            else:
                temp[char]=1
        return temp
 
    def checkDict(self, dict, str ):
        temp = self.createDict(str)
        return temp == dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictArray = []
        dictArray.append(self.createDict(strs[0]))
        for i in range(1,len(strs)):
            toChange = True
            for dict in dictArray:
                if self.checkDict(dict,strs[i]):
                    toChange = False
            
            if(toChange):
                dictArray.append(self.createDict(strs[i]))
                

        out = []
        lol = []
        for dict in dictArray:
            for str in strs:
                if(self.checkDict(dict,str)):
                    lol.append(str)
            out.append(lol)
            lol = []

        return out

        
# @lc code=end

