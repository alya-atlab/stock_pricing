def max_profit(prices):
    # min_price = min(prices)
    # max_price = max(prices[prices.index(min_price) :])
    count = 0
    profit = []
    for i in prices:
        min_price = i
        max_price = max(prices[count:])
        profit.append(max_price - min_price)
        count = count + 1

    return max(profit)


print(max_profit([2, 2, 3, 1, 4, 2, 4, 6, 1, 4]))
print("example 2:", max_profit([3, 10, 2, 4, 7]))
