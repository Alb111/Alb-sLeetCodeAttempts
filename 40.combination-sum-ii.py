from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        to_return: List[List[int]] = []
        candidates.sort()

        def backtrack(candidates: List[int], path: List[int]) -> None:

            # Base Case
            path_sum: int = sum(path)  
            if path_sum == target:
                to_return.append(path.copy())
                return

            # Define Choices
            for index, candidate in enumerate(candidates):

                if index > 0 and candidates[index] == candidates[index-1]:
                    continue # python for loop ingore changes to index!!

                if path_sum + candidate > target:
                    break

                path.append(candidate)
                backtrack(candidates = candidates[index+1:], path=path)
                path.pop()


        backtrack(candidates = candidates, path = [])
        return to_return

        



             


        
        
