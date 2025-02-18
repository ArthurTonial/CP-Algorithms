# https://neetcode.io/problems/buy-and-sell-crypto

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy= prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell - min_buy)
            min_buy = min(min_buy, sell)
        return max_profit
    
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r = 0, 1
#         max_profit = 0

#         while r < len(prices):
#             if prices[l] < prices[r]:
#                 max_profit = max(max_profit, prices[r] - prices[l])
#             else:
#                 l = r
#             r += 1
        
#         return max_profit
    