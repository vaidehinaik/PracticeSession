# solution 1

def buyAndSellStock(prices):
    buying_price  = min(prices)
    # print(buying_price)
    selling_price = max(prices[buying_price:])
    # print(selling_price)
    profit = selling_price - buying_price
    return profit
print("The maximum profit is: {}".format(buyAndSellStock([7,6,4,3,1])))



# soultion 2

# def buyAndSellStock(prices):

