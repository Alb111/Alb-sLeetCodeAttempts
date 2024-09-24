#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for num in nums:
            if(num in x):
                return True
            x.add(num)
        return False

        
# @lc code=end

