class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchase=prices[0]
        max_profit=0
        n=len(prices)
        for left in range(1,n):
            if purchase < prices[left]:
                profit = prices[left]-purchase
                if max_profit < profit:
                    max_profit=profit
            else:
                purchase=prices[left]
        return max_profit


