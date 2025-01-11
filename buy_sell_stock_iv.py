class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        buy = [float("inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                buy[j] = min(buy[j], price - sell[j - 1])
                sell[j] = max(sell[j], price - buy[j])

        return sell[k]

    # time complexity is O(n*k)
    # space complexity is O(k)
