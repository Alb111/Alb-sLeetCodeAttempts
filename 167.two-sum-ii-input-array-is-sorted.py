#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        cursum = -100
        while ( cursum != target):
            cursum = numbers[left] + numbers[right]
            if cursum > target:
                right-=1
            elif cursum < target:
                left+=1
            else:
                return [left+1, right+1]            
            

      
       
# @lc code=end

