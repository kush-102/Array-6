class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        return self.helper(prices, 0, -1, 0)

    def helper(self, prices, i, prev_buy, profit):
        if i >= len(prices):
            return profit
        result = 0
        if prev_buy == -1:
            result = max(
                self.helper(prices, i + 1, prev_buy, profit),
                self.helper(prices, i + 1, prices[i], profit),
            )

        else:
            result = max(
                self.helper(prices, i + 1, prev_buy, profit),
                self.helper(prices, i + 2, -1, profit + prices[i] - prev_buy),
            )
        return result
        # time complexity is O(2^n)
        # space complexity is O(n)
        # using memoization


class Solution:
    def __init__(self):
        self.memo = []

    def maxProfit(self, prices):
        n = len(prices)

        self.memo = [[-1] * 2 for _ in range(n)]
        return self.helper(prices, 0, 0)

    def helper(self, prices, i, state):
        # Base case
        if i >= len(prices):
            return 0

        if self.memo[i][state] != -1:
            return self.memo[i][state]

        # Recursive cases
        if state == 0:
            result = max(
                self.helper(prices, i + 1, 0), self.helper(prices, i + 1, 1) - prices[i]
            )
        else:
            result = max(
                self.helper(prices, i + 1, 1), self.helper(prices, i + 2, 0) + prices[i]
            )

        self.memo[i][state] = result
        return result


# time and space complexity is O(n)
