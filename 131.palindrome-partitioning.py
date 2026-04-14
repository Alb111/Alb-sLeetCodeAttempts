from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(str_under_test: str) -> bool:
            if len(str_under_test) == 0:
                return False 
        
            left: int = 0
            right: int = len(str_under_test) - 1
            while left < right:
                if str_under_test[left] != str_under_test[right]:
                    return False
                left+=1
                right-=1
            return True

        # IM DOING SOMETHING WRONG HERE I JUST NOT SURE WHAT
        def find_chars_used(path: List[int]) -> int:
            if len(path) == 0:
                return 0

            total_sum: int = 0
            prev = 0
            # for i in range(len(path) - 1):
            for i in path:
                total_sum += (i - prev)
                prev = i
            
            print(total_sum)
            return total_sum 
                    
            
        def backtrack(path: List[int], solution_set: List[List[str]]) -> None:

            print(path)

            # chars_used: int = 0 if len(path) == 0 else max(path)
            chars_used: int = find_chars_used(path)
            
            # we found a valid subset
            # if chars_used == len(s) - 1:
            if chars_used == len(s):
                print("this shit get hit")
                # build strs from path indices
                prev: int = 0 
                valid_subset: List[str] = []

                for i in path:
                    valid_subset.append(s[prev:i])
                    prev = i 

                print(valid_subset)

                # add valid subset to our solutions
                solution_set.append(valid_subset.copy())
                return

            
            start: int = 0 if len(path) == 0 else path[-1]
            for i in range(start, len(s) + 1):
                str_under_test: str = s[start:i]
                if isPalindrome(str_under_test):
                    path.append(i)
                    backtrack(path, solution_set)
                    path.pop()


        # main function 
        solution_set: List[List[str]] = []
        backtrack([],solution_set)
        return solution_set


x = Solution()
print(x.partition("bb"))
