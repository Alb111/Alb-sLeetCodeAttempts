#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        # go through and find prefix values
        temp = 1
        for i in range(len(nums)):
            prefix[i] =  temp;
            temp *= nums[i];

        #same thing bit backwards
        temp = 1
        for i in reversed(range(len(nums))):
            postfix[i] =  temp;
            temp *= nums[i];

        #go through and multply postfix and prefix stuff togoether
        out = [1] * len(nums)
        for i in range(len(nums)):
            out[i] = postfix[i] * prefix[i]

        return out





            
            
        
# @lc code=end

