#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            goal = target - num;
            # no reason to search for a nums that cant be in the list
            # if not (target>numbers[-1] or target<0):
            left, right = index + 1, len(numbers)-1

            while(left <= right):
                mid = left + (right - left)//2
                if numbers[mid] == goal:
                    # found match
                    return [index + 1, mid + 1]
                elif numbers[mid] > goal:
                    right = mid-1
                else:
                    left = mid + 1
                # no match found go to next element


       
# @lc code=end

