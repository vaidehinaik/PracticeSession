def calculate_proceeds(allotment, final_share_price):
    proceeds = int(allotment) * float(final_share_price)
    return proceeds

def calculate_cost(allotment, initial_share_price, buy_commission, sell_commission, tax_on_capital_gain):
    cost = allotment * initial_share_price + buy_commission + sell_commission + tax_on_capital_gain
    return cost
