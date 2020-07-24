class Stock_Profit_Calculator():

    def formatting_Decimal(number):
        return "%.2f" % number

    @staticmethod
    def calculate_Proceeds(final_Share_Price, allotment):
        return final_Share_Price * allotment

    @staticmethod
    def calculate_Cost(initial_Share_Price, allotment):
        return initial_Share_Price * allotment

    @staticmethod
    def calculate_Net_Profit(initial_Share_Price, final_Share_Price, allotment, buy_Commission, sell_Commission):
        return ((final_Share_Price - initial_Share_Price) * allotment)  - buy_Commission - sell_Commission

    @staticmethod
    def calculate_Return_On_Investment(profit, tax_rate):
        return profit * (tax_rate / 100)

    @staticmethod
    def calculate_Break_Even_Price(initial_Share_Price, allotment, buy_Commission, sell_Commission):
        return ((buy_Commission + sell_Commission) / allotment) + initial_Share_Price

if __name__ == '__main__':

    print ("Compute Your Profit:\n\n")
    ticker_Symbol = input("Ticker Symbol:\n")

    allotment = int(input("Allotment:\n"))

    final_Share_Price = float(input("Final Share Price:\n"))

    sell_Commission = float(input("Sell Commission:\n"))

    initial_Share_Price = float(input("Initial Share Price:\n"))

    buy_Commission = float(input("Buy Commission:\n"))

    tax_Rate = float(input("Capital Gain Tax Rate:\n"))

    purchase_Price = Stock_Profit_Calculator.calculate_Cost(initial_Share_Price, allotment)
    net_Profit = Stock_Profit_Calculator.calculate_Net_Profit(initial_Share_Price, final_Share_Price, allotment, buy_Commission, sell_Commission)
    tax = Stock_Profit_Calculator.calculate_Return_On_Investment(net_Profit, tax_Rate)
    cost = purchase_Price + buy_Commission + sell_Commission + tax
    netProfit = net_Profit - tax

    # display result
    print ("\n")
    print ("PROFIT REPORT:\n")
    proceeds = Stock_Profit_Calculator.formatting_Decimal(Stock_Profit_Calculator.calculate_Proceeds(final_Share_Price, allotment))

    print ("Proceeds ${}\n".format(proceeds))

    print ("Cost: ${}\n".format(cost))
    print ("=== Cost details ===\n")
    print ("Total Purchase Price:")
    print("{} x ${} = {}".format(allotment, allotment, purchase_Price))

    print ("Buy Commission = {}".format(Stock_Profit_Calculator.formatting_Decimal(buy_Commission)))

    print ("Sell Commission = {}".format(Stock_Profit_Calculator.formatting_Decimal(sell_Commission)))

    print ("Tax on Capital Gain = {}% of {} = {}".format(tax_Rate,
                                                         Stock_Profit_Calculator.formatting_Decimal(net_Profit),
                                                         Stock_Profit_Calculator.formatting_Decimal(tax)))

    print ("=== Net Profit ===")
    print ("${}".format(Stock_Profit_Calculator.formatting_Decimal(netProfit)))

    print ("=== Return on Investment ===")
    print ("{}%".format(Stock_Profit_Calculator.formatting_Decimal(100 + (netProfit - cost) / cost * 100)))

    print ("To break even, you should have a final share price:")
    break_even_price = Stock_Profit_Calculator.formatting_Decimal(Stock_Profit_Calculator.calculate_Break_Even_Price(initial_Share_Price, allotment, buy_Commission, sell_Commission))

    print ("${}".format(break_even_price))
