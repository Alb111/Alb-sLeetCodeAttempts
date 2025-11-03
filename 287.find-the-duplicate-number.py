class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we know a loop exits therefor we can infinite loop with
        # fylod algo
        slow: int = 0
        fast: int = 0
        while True:
            fast = (fast + 2) % len(nums)
            slow = (slow + 1) % len(nums)
            if nums[slow] == nums[fast]:
                break
        return nums[slow]




        

            
            

