class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length = len(prices)
        if length == 0: return 0

        #at least one element

        profitForward = []
        maxProfit = -1
        minPrice = prices[0]

        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(maxProfit, price - minPrice)
            profitForward.append(maxProfit)


        profitBackward = []

        maxProfit = -1
        maxPrice = prices[-1]

        for price in reversed(prices):
            maxPrice = max(maxPrice, price)
            maxProfit = max(maxProfit, maxPrice - price)
            profitBackward.insert(0, maxProfit)


        result = profitForward[-1]

        for i in range(length -1):
            result = max(result, profitForward[i] + profitBackward[i+1])
        return result
