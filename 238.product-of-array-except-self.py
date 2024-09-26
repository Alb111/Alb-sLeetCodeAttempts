#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = 0
        indexofZero = 0
        for index, num in enumerate(nums):
            if(num != 0):
                total *= num
            else:
                zeros +=1
                indexofZero = index
        
        out = [0] * len(nums) 
        #if we have more than one 0 then all zero
        if (zeros > 1):
            return [0]*len(nums)
        elif(zeros == 1):
            out[indexofZero] = total
            return out
        else:
            for index, num in enumerate(nums):
                out[index] = (int)(total/num)
            return out


            
            
        
# @lc code=end

