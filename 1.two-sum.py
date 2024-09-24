#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, num in enumerate(nums):
            if num in diffs:
                return [diffs[num], i]
            diffs[target-num] = i;
        return -1


            

        
         
        
# @lc code=end

