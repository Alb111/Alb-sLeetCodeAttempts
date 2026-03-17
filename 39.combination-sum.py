from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        to_return: List[List[int]] = []

        candidates.sort()
        
        def backtrack(path: List[int], choices: List[int]) -> None:
            # Base Case
            path_sum: int = sum(path)
            if path_sum == target:
                to_return.append(path.copy())
                return

            for index, choice in enumerate(choices):

                if path_sum + choice > target:
                    break

                path.append(choice)
                backtrack(path, choices[:index+1])
                path.pop()

        backtrack([], candidates)

        return to_return
        
        
