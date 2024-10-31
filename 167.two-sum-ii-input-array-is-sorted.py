#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numtoIndex ={}
        for index, num in enumerate(numbers):
            if((target-num) in numtoIndex):
                return [numtoIndex[target-num]+1, index+1]
            numtoIndex[num] = index
        
# @lc code=end

