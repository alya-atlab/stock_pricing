def max_profit(prices):
    min_price = min(prices)
    max_price = max(prices[prices.index(min_price) :])
    return max_price - min_price


print(max_profit([2, 2, 3, 1, 4, 2, 4, 6, 1, 4]))
