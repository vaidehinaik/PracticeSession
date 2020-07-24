
class Stock_Profit_Calculator():

    def formatTwoDecimalPoints(floatNum):
        """Return a string of the float number with only two decimal points."""
        return "%.2f" % floatNum

    @staticmethod
    def calculate_Proceeds(final_Share_Price, allotment):
        return final_Share_Price * allotment

    @staticmethod
    def calculate_Cost(initial_Share_Price, allotment):
        return initial_Share_Price * allotment

    @staticmethod
    def calculate_Net_Profit(initial_Share_Price, final_Share_Price, allotment, buy_Commission, sell_Commission):
        return (final_Share_Price - initial_Share_Price) * allotment  - buy_Commission - sell_Commission

    @staticmethod
    def calculate_Return_On_Investment(net_profit, cost):
        return net_profit/cost*100

    @staticmethod
    def calculate_Break_Even_Price(initial_Share_Price, allotment, buy_Commission, sell_Commission):
        return (buy_Commission + sell_Commission) / allotment + initial_Share_Price
        # print ("Compute Your Profit:\n\n")
        # ticker_Symbol = input("Ticker Symbol:\n")
        # allotment = int(input("Allotment:\n"))
        # final_Share_Price = float(input("Final Share Price:\n"))
        # # print formatTwoDecimalPoints(finalSharePrice) + "\n\n"
        # sell_Commission = float(input("Sell Commission:\n"))
        # initial_Share_Price = float(input("Initial Share Price:\n"))
        # buy_Commission = float(input("Buy Commission:\n"))
        # tax_Rate = float(input("Capital Gain Tax Rate:\n"))

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
    net_Profit = net_Profit - tax

    # display result
    print ("\n")
    print ("PROFIT REPORT:\n")
    print ("Proceeds\n")
    print ("$" + Stock_Profit_Calculator.formatTwoDecimalPoints(Stock_Profit_Calculator.calculate_Proceeds(final_Share_Price, allotment)) + "\n\n")
    print ("Cost\n")
    print ("$" + str(cost) + "\n\n")
    print ("Cost details:\n")
    print ("Total Purchase Price:\n")
    print (str(allotment) + " x " + "$" + str(allotment) + " = " + str(purchase_Price) + "\n")
    print ("Buy Commission = " + Stock_Profit_Calculator.formatTwoDecimalPoints(buy_Commission) + "\n")
    print ("Sell Commission = " + Stock_Profit_Calculator.formatTwoDecimalPoints(sell_Commission) + "\n")
    print ("Tax on Capital Gain = " + str(tax) + "%" + " of " + "$" + Stock_Profit_Calculator.formatTwoDecimalPoints(net_Profit) + " = " + Stock_Profit_Calculator.formatTwoDecimalPoints(tax) + "\n\n")
    print ("Net Profit:\n")
    print ("$" + Stock_Profit_Calculator.formatTwoDecimalPoints(net_Profit) + "\n\n")
    print ("Return on Investment:\n")
    print (Stock_Profit_Calculator.formatTwoDecimalPoints(100 + (net_Profit - cost) / cost * 100) + "%" + "\n")
    print ("To break even, you should have a final share price of \n")
    print ("$" + Stock_Profit_Calculator.formatTwoDecimalPoints(Stock_Profit_Calculator.calculate_Break_Even_Price(initial_Share_Price, allotment, buy_Commission, sell_Commission)))

