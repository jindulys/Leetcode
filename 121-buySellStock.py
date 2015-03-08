class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        low = 0
        high = 0

        currentMax = 0
        result = []
        for i in range(n):
            if prices[i] >= prices[high]:
                high = i
                print 'low is : '+ str(low)
                print 'high is : '+ str(high)
                currentMax = prices[high] - prices[low]
            if prices[i] < prices[low]:
                result.append(currentMax)
                low = i
                high = i
                print 'low is : '+ str(low)
                print 'high is : '+ str(high)
                currentMax = 0

        result.append(currentMax)

        result.sort()
        return result[-1]

    # http://chaoren.is-programmer.com/posts/43595
    def maxProfitKitt(self, prices):
        if not prices: return 0
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit

if __name__ == '__main__':
    s = Solution()
    m = s.maxProfit([4,1,2])
    print m
