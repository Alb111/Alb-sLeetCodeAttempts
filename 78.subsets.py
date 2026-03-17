from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        to_return: List[List[int]] = []

        def backtrack(path: List[int], choice_start: int):
            to_return.append(path.copy())

            for i in range(choice_start, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return to_return

            

x: Solution = Solution()
print(x.subsets([1, 2, 3]))
