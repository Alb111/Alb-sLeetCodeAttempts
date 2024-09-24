#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import Dict
from typing import List


class Solution:
    def createDict(self, str):
        temp = [0]*26
        for char in str:
            temp[ord(char)-97]+=1
        return tuple(temp)
 

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out: Dict[tuple, List[str]] = {}
        for str in strs:
            temp = self.createDict(str);
            if( temp in out ):
                out[temp].append(str)
            else:
                out[temp] = []
                out[temp].append(str)
        
        return list(out.values())



                

        
# @lc code=end

