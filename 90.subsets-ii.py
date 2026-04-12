from typing import List, Set

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        def backtrack(current_path: List[int], index_to_start: int, output_list: List[List[int]]) -> None:
            output_list.append(current_path.copy())
            
            for i in range(index_to_start, len(nums)):
                # Skip duplicates
                if i > index_to_start and nums[i] == nums[i - 1]:
                    continue

                current_path.append(nums[i])
                backtrack(current_path, i + 1, output_list)
                current_path.pop()
                    

        output_list: List[List[int]] = []
        backtrack([], 0, output_list)
        return output_list
        
