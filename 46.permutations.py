from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation_len: int = len(nums)
        permutations: List[List[int]] = []
        used_choices: set[int] = set()        

        def backtrack(path: List[int]):

            if permutation_len == len(path):
                permutations.append(path.copy())

            for choice in nums:
                if choice not in used_choices:
                    path.append(choice) 
                    used_choices.add(choice)
                    backtrack(path)
                    path.pop()
                    used_choices.remove(choice)

        backtrack([])
        return permutations
