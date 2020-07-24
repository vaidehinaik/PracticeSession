import sys

def bestTimetoBuySellStock(prices):
    result,min_price = 0, sys.maxsize
    for price in prices:
        if price < min_price:
            min_price = price

        else:
            # result = max(result,price-min_price)
            if result < (price - min_price):
                result = price - min_price
    return result
print(bestTimetoBuySellStock([7,6,4,3,1]))



