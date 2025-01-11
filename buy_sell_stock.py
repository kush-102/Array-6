class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini = float("inf")
        profit = 0

        for i in range(n):
            mini = min(mini, prices[i])
            profit = max(profit, prices[i] - mini)
        return profit

    # time complexity is O(n)
    # space complexity is O(n)
