#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        nums.sort()
        output = []

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index -1]:
                continue 
                #skips repeats for starter pointer

            left, right = index+1, len(nums)-1
            while( left < right ):
                threeSum = num + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    output.append([num, nums[left], nums[right]])
                    left +=1
                    while nums[left] == nums[left - 1]:
                        left +=1
            return output
        


       
# @lc code=end

