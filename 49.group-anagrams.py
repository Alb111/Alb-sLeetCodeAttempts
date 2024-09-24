#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def createDict(self, str):
        temp = [0]*26
        for char in str:
            temp[ord(char)-97]+=1
        return temp
 

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        used = [False] * len(strs)
        for i in range(len(strs)):
            temp=[]
            if(not used[i]):
                str1 = self.createDict(strs[i])
                temp.append(strs[i])
                used[i] = True
                for k in range(i+1, len(strs)):
                    str2 = self.createDict(strs[k])
                    if(str1 == str2):
                        temp.append(strs[k])
                        used[k] = True
                out.append(temp)
        return out

                

        
# @lc code=end

