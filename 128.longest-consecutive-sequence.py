#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        longest = 1
        temp = 1
        numSet = set(nums)
        for num in numSet:
            if num - 1 not in numSet and num+1 in numSet:
                while(num+1 in numSet):
                    temp+=1
                    num+=1
                longest = max(longest, temp)
                temp = 1
        return longest
                            
                
                

                        
        
# @lc code=end

