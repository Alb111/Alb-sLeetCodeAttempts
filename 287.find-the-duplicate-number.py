class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sum all the numbers and find the max
        total: int = 0
        max_n: int = -1
        for num in nums:
            max_n = max(max_n, num)
            total += num

        # calc the expected sum
        exp_sum: int = max_n * (1+max_n)/2
        num_repeats: int = len(nums) - max_n  

        return (total - exp_sum) / num_repeats

