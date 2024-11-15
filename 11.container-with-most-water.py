#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0;
        for i in range(len(height)):
            for j in range(i,len(height)):
                tempVol = (j-i)*min(height[j], height[i]) 
                maxVol = max(maxVol, tempVol)
        return maxVol
        
# @lc code=end

