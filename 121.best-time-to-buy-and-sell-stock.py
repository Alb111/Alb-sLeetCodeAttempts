#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        out = 0
        
        while right < len(prices):
            # If there's a profit opportunity
            if prices[left] < prices[right]:
                out = max(out, prices[right] - prices[left])
            else:
                # Move the left pointer to the right's position
                left = right
            right += 1
        
        return out

                
        

                

            
            
            
        
# @lc code=end

