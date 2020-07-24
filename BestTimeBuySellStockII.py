import sys
def bestTimeBuySellStockII(prices):
    min_price = sys.maxsize
    max_profit_arr = []
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit_arr.append(price-min_price)
            min_price = price
    return sum(max_profit_arr)
print(bestTimeBuySellStockII([7,6,4,3,1]))


