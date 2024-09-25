#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numtoOccurance = {}
        for num in nums:
            numtoOccurance[num] = 1+numtoOccurance.get(num,0)

        occurance = []
        for i in range(len(nums)+1):
            occurance.append([])

        for num in numtoOccurance:
            occurance[numtoOccurance[num]].append(num)


        result = []
        for i in range(len(occurance) - 1, 0, -1):
            for num in occurance[i]:
                result.append(num)
                if len(result) == k:
                    return result

        
# @lc code=end

