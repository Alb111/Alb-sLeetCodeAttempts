#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if(len(s)!=len(t)):
           return False
       
       sDict,tDict = {},{}

        #fill with counts of chars
       for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]]+=1
            else:
                sDict[s[i]]=1

            if t[i] in tDict:
                tDict[t[i]]+=1
            else:
                tDict[t[i]]=1
        
        #compare
       for key in sDict:
           if key in tDict:
               if sDict[key] != tDict[key]:
                   return False
           else:
               return False;
                
        
       return True

            
           
           

# @lc code=end

