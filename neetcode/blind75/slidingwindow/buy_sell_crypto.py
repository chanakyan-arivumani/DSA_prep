class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # prices = [10,1,5,6,7,1]
        sell = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > buy and prices[i] > sell:
                sell = prices[i]
            else:
                buy = prices[i]
            print(f"buy: {buy} sell: {sell}")
        if buy < sell:
            return sell - buy
        return 0
