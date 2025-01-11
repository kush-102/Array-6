class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # exhaustive method
        n = len(prices)
        profit1 = 0
        profit2 = 0
        profit = 0

        for i in range(n):  # Two transactions
            profit1 = self.helper(prices, 0, i)  # Profit for the first transaction
            profit2 = self.helper(prices, i, n)  # Profit for the second transaction
            profit = max(profit, profit1 + profit2)

        return profit

    def helper(self, prices, low, high):
        mini = float("inf")
        profit = 0

        for i in range(low, high):
            mini = min(mini, prices[i])  # Track the minimum price
            profit = max(profit, prices[i] - mini)  # Calculate max profit

        return profit
        # time complexity is O(n^2)
        # space complexity is O(1)

        # buy1 and sell1 maintains single best transaction
        # effective buying  price and sell2 maintains best profit of both transaction

        buy1 = prices[0]
        sell1 = 0
        buy2 = prices[0]
        sell2 = 0

        for i in range(1, n):
            buy1 = min(buy1, prices[i])
            sell1 = max(sell1, prices[i] - buy1)

            buy2 = min(buy2, prices[i] - sell1)
            sell2 = max(sell2, prices[i] - buy2)
        return sell2

    # time complexity is O(n)
    # space complexity is O(1)
